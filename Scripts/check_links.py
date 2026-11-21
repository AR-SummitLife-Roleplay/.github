"""Check that every relative link in a repository's Markdown points at a real file and heading.

Usage: python3 -I check_links.py [repository folder]
The folder defaults to the current one. Only files Git tracks are checked.
Exits with status 1 and lists each broken link if any are found.
"""
import re
import sys
from pathlib import Path

# Isolated mode (python3 -I) leaves this folder off the import path, so add it back.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from repository_files import tracked_files  # noqa: E402

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")


def slug(text):
    """GitHub-style heading anchor."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def prose_lines(path):
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield number, line


def anchors(path, cache={}):
    if path not in cache:
        seen, found = {}, set()
        for _, line in prose_lines(path):
            m = HEADING.match(line)
            if m:
                base = slug(m.group(1))
                count = seen.get(base, 0)
                found.add(base if count == 0 else f"{base}-{count}")
                seen[base] = count + 1
        cache[path] = found
    return cache[path]


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    broken = []
    for md in tracked_files(root, suffixes={".md"}):
        for number, line in prose_lines(md):
            for target in LINK.findall(line):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue  # external link or mail address
                file_part, _, anchor = target.partition("#")
                dest = md if not file_part else (md.parent / file_part).resolve()
                where = f"{md.relative_to(root)}:{number}"
                if not dest.exists():
                    broken.append(f"{where}: missing file {target}")
                elif anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                    broken.append(f"{where}: missing heading {target}")
    for b in broken:
        print(b)
    print(f"{len(broken)} broken link(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
