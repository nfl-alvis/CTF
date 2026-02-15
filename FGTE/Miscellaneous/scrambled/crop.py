from PIL import Image
import os, sys

inp = sys.argv[1]
os.makedirs("out", exist_ok=True)

img = Image.open(inp)
w, h = img.size

cols = rows = 4
tw, th = w // cols, h // rows

idx = 1
for r in range(rows):
    for c in range(cols):
        tile = img.crop((c*tw, r*th, (c+1)*tw, (r+1)*th))
        tile.save(f"out/part_{idx:02d}.png")
        idx += 1
