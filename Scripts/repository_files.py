"""Shared helper for the check scripts: list the files Git tracks in a repository."""
import subprocess
from pathlib import Path

# Where the shared workflows check out this repository's scripts inside the calling repository.
SHARED_SCRIPTS_CHECKOUT = ".caldera-ci"


def tracked_files(root, suffixes=None):
    """Return tracked files under root, sorted, optionally limited to the given suffixes.

    Files staged for deletion or missing from disk are skipped.
    """
    output = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8")
    files = []
    for name in output.split("\0"):
        if not name or name.startswith(SHARED_SCRIPTS_CHECKOUT + "/"):
            continue
        path = Path(root) / name
        if not path.is_file():
            continue
        if suffixes and path.suffix.lower() not in suffixes:
            continue
        files.append(path)
    return sorted(files)


def lfs_files(root):
    """Return the tracked files that .gitattributes sends through Git LFS."""
    names = [str(p.relative_to(root)) for p in tracked_files(root)]
    if not names:
        return set()
    output = subprocess.run(
        ["git", "-C", str(root), "check-attr", "-z", "--stdin", "filter"],
        input="\0".join(names).encode("utf-8"),
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8")
    parts = output.split("\0")
    lfs = set()
    for i in range(0, len(parts) - 2, 3):
        if parts[i + 2] == "lfs":
            lfs.add(Path(root) / parts[i])
    return lfs
