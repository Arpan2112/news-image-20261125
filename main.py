#!/usr/bin/env python3
"""Entry for make.fun competition news-image-20261125.

Writes the repository's entry.png to /output/entry.png, byte for byte.
No network, no randomness: two runs always produce identical bytes.
"""

import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
