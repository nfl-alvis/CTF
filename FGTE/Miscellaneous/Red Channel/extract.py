from PIL import Image
import glob

files = sorted(glob.glob("img_*.png"))

for f in files:
    im = Image.open(f).convert("RGB")
    w, h = im.size
    px = im.load()

    data = bytearray()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            data.append(r)

    # cari karakter printable pertama
    for b in data:
        if 32 <= b <= 126:
            print(chr(b), end="")
            break

print()
