"""Check formatting and that every JSON and YAML file parses.

Usage: python3 -I check_formatting.py [repository folder]
Needs PyYAML. Rules match each repository's .editorconfig and .gitattributes:
- no trailing whitespace (Markdown excepted);
- every text file ends with a newline;
- Windows line endings only in .ps1, .bat and .cmd files;
- Enforce Script (.c) lines are indented with tabs, not spaces.
Files Workbench writes itself and files stored in Git LFS are left alone.
Exits with status 1 and lists each problem if any are found.
"""
import json
import sys
from pathlib import Path

import yaml

# Isolated mode (python3 -I) leaves this folder off the import path, so add it back.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from repository_files import lfs_files, tracked_files  # noqa: E402

WORKBENCH_WRITTEN = {".et", ".ent", ".conf", ".layout", ".meta", ".emat", ".gproj"}
CRLF_ALLOWED = {".ps1", ".bat", ".cmd"}
NO_TRIM = {".md"}


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skip = lfs_files(root)
    problems = []
    checked = 0
    for path in tracked_files(root):
        if path in skip or path.suffix.lower() in WORKBENCH_WRITTEN:
            continue
        data = path.read_bytes()
        if b"\0" in data[:8000]:
            continue  # binary file
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(f"{path.relative_to(root)}: not UTF-8 text")
            continue
        checked += 1
        name = str(path.relative_to(root))
        suffix = path.suffix.lower()
        if text and not text.endswith("\n"):
            problems.append(f"{name}: no newline at end of file")
        if "\r\n" in text and suffix not in CRLF_ALLOWED:
            problems.append(f"{name}: Windows line endings")
        for number, line in enumerate(text.splitlines(), 1):
            if suffix not in NO_TRIM and line != line.rstrip(" \t"):
                problems.append(f"{name}:{number}: trailing whitespace")
            if suffix == ".c" and line.startswith("    "):
                problems.append(f"{name}:{number}: indented with spaces, not tabs")
        try:
            if suffix == ".json":
                json.loads(text)
            elif suffix in {".yml", ".yaml"}:
                list(yaml.safe_load_all(text))  # files may hold several YAML documents
        except (ValueError, yaml.YAMLError) as error:
            problems.append(f"{name}: does not parse: {error}".splitlines()[0])
    for p in problems:
        print(p)
    print(f"{checked} file(s) checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
