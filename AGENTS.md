# Learning Notes

Write mathematical learning notes in Typst, primarily in Traditional Chinese
with natural English technical terms. HTML is the primary reading format.
The human writes first; collaborate through conversation when asked to extend.

## View & Extend

When the user invokes `Agent View & Extend` or `$agent-view-extend`, read
`skills/agent-view-extend/SKILL.md` and follow it. The skill lives in this regular
directory because this workspace currently disallows writing `.agents/`.
This routing works through this file; native skill-picker discovery is not yet
installed or verified. Do not claim there is a clickable button.

## Files and checks

- `index.typ` is the entrypoint; `notes/*.typ` holds included notes.
- Follow ordinary Typst headings, labels and references. Do not require special
  Agent annotations, parallel Markdown source, or a fixed lesson schema.
- Run `python3 scripts/build.py` and `python3 scripts/check_site.py` after changes.
- `python3 scripts/preview.py` serves the site locally and rebuilds on changes;
  the browser currently requires a manual refresh.
- Keep assets referenced by Typst inside the repository. HTML export embeds
  assets; if adding a raw HTML URL, ensure its target is published in `_site`.
- Keep generated `_site/` out of Git. Actions pins Typst to 0.15.1; update the
  version deliberately after checking representative math and references.
- Compilation validates syntax and output, not mathematical truth. Inspect
  assumptions and important derivations separately.
- Only commit or push when the user asks; invoking the extension skill does not
  itself request publication. Never overwrite concurrent human edits.
