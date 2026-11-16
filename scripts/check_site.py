#!/usr/bin/env python3
"""Check the built HTML's local links, anchors, and assets before deployment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import SITE


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicates = set()
        self.links = []
        self.tags = set()

    def handle_starttag(self, tag, attributes):
        self.tags.add(tag)
        attrs = dict(attributes)
        identifier = attrs.get("id")
        if identifier:
            if identifier in self.ids:
                self.duplicates.add(identifier)
            self.ids.add(identifier)
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

    handle_startendtag = handle_starttag


def check():
    pages = {}
    errors = []
    for path in SITE.rglob("*.html"):
        page = Page()
        page.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = page
        if not {"html", "head", "title", "body"} <= page.tags:
            errors.append(f"{path.name}: missing HTML document structure")
        if page.duplicates:
            errors.append(f"{path.name}: duplicate IDs {sorted(page.duplicates)}")
    if (SITE / "index.html").resolve() not in pages:
        errors.append("missing index.html")
    if not (SITE / "styles.css").is_file():
        errors.append("missing styles.css")
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith("/"):
                errors.append(f"{path.name}: root-relative URL breaks project Pages: {link}")
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target = target / "index.html"
            if not target.is_relative_to(SITE.resolve()) or not target.is_file():
                errors.append(f"{path.name}: missing local target: {link}")
            elif url.fragment and target in pages:
                if unquote(url.fragment) not in pages[target].ids:
                    errors.append(f"{path.name}: unresolved anchor: {link}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(pages)} HTML page(s): local links, anchors and assets OK.")


if __name__ == "__main__":
    check()
