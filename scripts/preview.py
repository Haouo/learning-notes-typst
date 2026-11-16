#!/usr/bin/env python3
"""Serve locally and rebuild when Typst, CSS or local assets change."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import subprocess
import threading

from build import ROOT, SITE, build


def snapshot():
    files = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part.startswith(".") or part in {"_site", "__pycache__"}
               for part in relative.parts):
            continue
        if path.is_file():
            stat = path.stat()
            files.append((str(relative), stat.st_mtime_ns, stat.st_size))
    return sorted(files)


def watch(stop):
    previous = snapshot()
    while not stop.wait(0.6):
        try:
            current = snapshot()
            if current != previous:
                previous = current
                try:
                    build()
                except (RuntimeError, subprocess.CalledProcessError, OSError) as error:
                    print(f"編譯失敗，保留前次預覽：{error}", flush=True)
        except FileNotFoundError:
            continue  # An editor may atomically replace a file during the scan.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    build()
    handler = partial(SimpleHTTPRequestHandler, directory=str(SITE))
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    except PermissionError:
        raise SystemExit("此環境不允許啟動本機伺服器；請在自己的 terminal 執行，或直接開啟 _site/index.html。")
    stop = threading.Event()
    worker = threading.Thread(target=watch, args=(stop,), daemon=True)
    worker.start()
    print(f"預覽：http://127.0.0.1:{args.port}（儲存後重建；請刷新瀏覽器）", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        worker.join()
        server.server_close()
