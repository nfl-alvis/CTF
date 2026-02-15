from PIL import Image
import sys

pos_to_tile = {
  1:13, 2:15, 3:9, 4:1,
  5:14, 6:16, 7:10, 8:2,
  9:3, 10:11, 11:5, 12:7,
  13:4, 14:12, 15:6, 16:8
}

img = Image.open(sys.argv[1])
w, h = img.size

tw, th = w // 4, h // 4

tiles = {}
idx = 1
for r in range(4):
    for c in range(4):
        tiles[idx] = img.crop((c*tw, r*th, (c+1)*tw, (r+1)*th))
        idx += 1

out = Image.new("RGB", (tw * 4, th * 4))

for pos in range(1, 17):
    r, c = divmod(pos - 1, 4)
    out.paste(tiles[pos_to_tile[pos]], (c * tw, r * th))

out.save("recovered.png")
print("[+] saved recovered.png")
