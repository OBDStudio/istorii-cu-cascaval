"""Resize + recompress Figma-exported photos for web delivery.

Usage: python optimize.py <max_width> <file> [file ...]
Overwrites each file in place as JPEG (or keeps PNG when it has alpha).
"""
import os
import sys

from PIL import Image


def optimize(path, max_w):
    im = Image.open(path)
    orig_size = os.path.getsize(path)
    has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)

    if im.width > max_w:
        h = round(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)

    root, _ = os.path.splitext(path)
    if has_alpha:
        out = root + ".png"
        im.save(out, "PNG", optimize=True)
    else:
        out = root + ".jpg"
        im.convert("RGB").save(out, "JPEG", quality=82, optimize=True, progressive=True)

    if out != path:
        os.remove(path)
    print(f"{os.path.basename(path)} -> {os.path.basename(out)} "
          f"{im.size}  {orig_size/1024:.0f}KB -> {os.path.getsize(out)/1024:.0f}KB")


if __name__ == "__main__":
    width = int(sys.argv[1])
    for f in sys.argv[2:]:
        optimize(f, width)
