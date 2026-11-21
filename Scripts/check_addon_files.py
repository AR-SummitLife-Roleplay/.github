"""Check an addon repository's file and folder names and its large files.

Usage: python3 -I check_addon_files.py [repository folder]
- Folder names use PascalCase letters and digits only: no spaces, dots, dashes or underscores.
  GitHub's own folders (.github, ISSUE_TEMPLATE, workflows) are allowed.
- File names have no spaces.
- Every file .gitattributes sends to Git LFS is committed as an LFS pointer, never as the file itself.
- No other file is larger than the limit below.
Exits with status 1 and lists each problem if any are found.
"""
import re
import sys
from pathlib import Path

# Isolated mode (python3 -I) leaves this folder off the import path, so add it back.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from repository_files import lfs_files, tracked_files  # noqa: E402

# [Assumed] Largest file allowed outside Git LFS. Bigger files belong in Git LFS.
MAX_NON_LFS_BYTES = 5 * 1024 * 1024
FOLDER_NAME = re.compile(r"^[A-Z][A-Za-z0-9]*$")
GITHUB_FOLDERS = {".github", "ISSUE_TEMPLATE", "workflows"}
LFS_POINTER = b"version https://git-lfs.github.com/spec/v1\n"


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    lfs = lfs_files(root)
    problems = []
    folders = set()
    files = tracked_files(root)
    for path in files:
        relative = path.relative_to(root)
        folders.update(relative.parents)
        if " " in path.name:
            problems.append(f"{relative}: file name has a space")
        size = path.stat().st_size
        if path in lfs:
            with path.open("rb") as handle:
                if handle.read(len(LFS_POINTER)) != LFS_POINTER:
                    problems.append(f"{relative}: committed directly, not as a Git LFS pointer")
        elif size > MAX_NON_LFS_BYTES:
            problems.append(f"{relative}: {size // 1024} KiB, over the limit for files outside Git LFS")
    for folder in sorted(folders):
        if folder == Path("."):
            continue
        if folder.name not in GITHUB_FOLDERS and not FOLDER_NAME.match(folder.name):
            problems.append(f"{folder}/: folder name is not PascalCase letters and digits")
    for p in problems:
        print(p)
    print(f"{len(files)} file(s) and {len(folders) - 1 if folders else 0} folder(s) checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
