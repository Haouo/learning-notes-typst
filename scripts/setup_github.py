#!/usr/bin/env python3
"""Create the public repository, enable Actions-based Pages, and push main."""
import json
import subprocess

from build import ROOT, build
from check_site import check


def run(*args, capture=False, check=True):
    return subprocess.run(args, cwd=ROOT, check=check, text=True,
                          stdout=subprocess.PIPE if capture else None)


def setup():
    build()
    check()
    run("gh", "auth", "status")
    owner = run("gh", "api", "user", "--jq", ".login", capture=True).stdout.strip()
    repository = f"{owner}/learning-notes-typst"
    if not (ROOT / ".git").exists():
        run("git", "init", "-b", "main")
    branch = run("git", "branch", "--show-current", capture=True).stdout.strip()
    if branch != "main":
        raise RuntimeError("目前分支不是 main；請先確認要發布的分支。")
    remote = run("git", "remote", "get-url", "origin", capture=True, check=False)
    if remote.returncode == 0:
        url = remote.stdout.strip()
        allowed = {f"https://github.com/{repository}.git",
                   f"https://github.com/{repository}",
                   f"git@github.com:{repository}.git"}
        if url not in allowed:
            raise RuntimeError(f"origin 不是預期的 {repository}；停止，未修改遠端。")
        visibility = run("gh", "repo", "view", repository, "--json", "visibility",
                         capture=True).stdout
        if json.loads(visibility)["visibility"] != "PUBLIC":
            raise RuntimeError("既有 repository 不是公開的；停止，未變更其可見性。")
    else:
        # gh repo create fails on a name collision; never reuse an unrelated repo.
        run("gh", "repo", "create", repository, "--public", "--source", str(ROOT),
            "--remote", "origin", "--description",
            "Human-Agent collaborative learning notes in Typst")
    run("git", "add", "--", "index.typ", "notes", "styles", "scripts", "skills",
        "AGENTS.md", "README.md", ".github", ".gitignore")
    staged = run("git", "diff", "--cached", "--quiet", check=False)
    if staged.returncode == 1:
        run("git", "commit", "-m", "Set up collaborative Typst notes and HTML publication")
    elif staged.returncode != 0:
        raise RuntimeError("無法確認 staged changes，停止發布。")
    # A default branch must exist before GitHub can configure its Pages environment.
    run("git", "push", "-u", "origin", "main")
    page = run("gh", "api", f"repos/{repository}/pages", capture=True, check=False)
    if page.returncode == 0:
        run("gh", "api", "--method", "PUT", f"repos/{repository}/pages",
            "-f", "build_type=workflow")
    else:
        run("gh", "api", "--method", "POST", f"repos/{repository}/pages",
            "-f", "build_type=workflow")
    # Explicitly rerun after Pages is enabled to avoid a first-push setup race.
    run("gh", "workflow", "run", "pages.yml", "--ref", "main")
    print(f"Repository: https://github.com/{repository}")
    print(f"Actions: https://github.com/{repository}/actions")
    print(f"部署成功後的網址：https://{owner.lower()}.github.io/learning-notes-typst/")


if __name__ == "__main__":
    try:
        setup()
    except (RuntimeError, subprocess.CalledProcessError, OSError) as error:
        raise SystemExit(f"首次發布未完成：{error}")
