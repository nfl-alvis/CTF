import re
import base64

data = open("output.txt", "r", encoding="utf-8", errors="ignore").read()

parts = re.findall(r"IDX:(\d{1,3})/(\d+)\|([A-Za-z0-9+/=]+)", data)

if not parts:
    print("GAK ADA CHUNK KEBACA")
    exit()

total_expected = int(parts[0][1])

# map idx -> chunk
mp = {}
for idx, total, chunk in parts:
    mp[int(idx)] = chunk

missing = [i for i in range(total_expected) if i not in mp]

print("Expected:", total_expected)
print("Got:", len(mp))
print("Missing:", missing)

b64 = "".join(mp[i] for i in range(total_expected))

# padding
b64 += "=" * ((4 - len(b64) % 4) % 4)

raw = base64.b64decode(b64)
open("recovered.jpg", "wb").write(raw)

print("Saved -> recovered.jpg")
