import cv2
import glob
from pyzbar.pyzbar import decode

frames = sorted(glob.glob("frames/*.png"))

seen = set()
results = []

for i, f in enumerate(frames):
    img = cv2.imread(f)
    if img is None:
        continue

    # upscale biar QR kebaca
    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    # grayscale + threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    qr = decode(th)
    if not qr:
        continue

    data = qr[0].data.decode(errors="ignore")

    if data not in seen:
        seen.add(data)
        results.append(data)
        print(data)

print("\nTOTAL UNIQUE:", len(results))
