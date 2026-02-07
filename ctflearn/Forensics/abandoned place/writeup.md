# Abandoned Place

## Challenge

the flag is outside of the pic, try to find it.  
another hint: dimensions, dimensions, everything is in dimensions.

File challenge:  
[abondoned_street_challenge2.jpg](https://ctflearn.com/challenge/download/1000)

---

## Analisis

Diberikan sebuah file gambar bernama `abondoned_street_challenge2.jpg`.  
Saat dibuka secara normal, tidak ditemukan hal mencurigakan secara visual.

![abondoned_street_challenge2.jpg](abondoned_street_challenge2.jpg)

Namun, berdasarkan hint yang diberikan yaitu **"dimensions"**, dapat diasumsikan bahwa data tersembunyi berada di luar area gambar yang sedang ditampilkan. Teknik umum pada challenge seperti ini adalah dengan **memanipulasi metadata dimensi gambar** (width/height), sehingga sebagian pixel tersembunyi tidak ikut dirender oleh viewer biasa.

Dengan kata lain: **file gambar menyimpan pixel lebih banyak daripada yang ditampilkan**, dan kita perlu mengubah dimensi agar seluruh data pixel dapat terlihat.

---

## Eksploitasi / Solusi

Untuk mengubah dimensi gambar, saya menggunakan script Python `modsize.py` yang tersedia di GitHub:

- Referensi script: https://github.com/flawwan/modsize/blob/master/modsize.py

Script tersebut bekerja dengan cara:
1. Membaca file gambar dalam bentuk bytes.
2. Menemukan offset header yang menyimpan nilai width dan height.
3. Mengubah nilai tersebut ke dimensi baru.
4. Menyimpan hasilnya menjadi file output.

Script yang digunakan:

```python
import argparse
import os
from subprocess import call

import filetype
from loguru import logger

rot_value = 0  # Default value
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Filepath to image")
parser.add_argument("output", help="Filepath to image")
parser.add_argument("--width", "-sw", type=int, help="New width of image")
parser.add_argument("--height", "-sh", type=int, help="New height of image")
args = parser.parse_args()


def modify_file(offset1, offset2, filename, output, width=None, height=None):
    logger.info("Loading image")
    bin_arr = []
    with open(filename, "rb") as f:
        arr = f.read()
    for b in arr:
        bin_arr.append(b)

    org_width = hex(int(hex(bin_arr[offset1])[2:] + hex(bin_arr[offset1 + 1])[2:], 16))
    org_height = hex(int(hex(bin_arr[offset2])[2:] + hex(bin_arr[offset2 + 1])[2:], 16))

    logger.info("Image loaded!")
    logger.info("Detected width: %d px" % int(org_width, 16))
    logger.info("Detected height: %d px" % int(org_height, 16))

    if width is None and height is None:
        logger.warning("Nothing todo. Set width/height?")
        exit()

    if width is None:
        width = int(org_width, 16)
    if height is None:
        height = int(org_height, 16)

    new_width = str(hex(width))[2:].zfill(4)
    new_height = str(hex(height))[2:].zfill(4)

    if str(org_width)[2:] != new_width:
        logger.info("New width: %d px" % int(new_width, 16))
    if str(org_height)[2:] != new_height:
        logger.info("New height: %d px" % int(new_height, 16))

    # Set width
    bin_arr[offset1] = int(str(new_width)[:2], 16)
    bin_arr[offset1 + 1] = int(str(new_width)[2:], 16)

    # Set height
    bin_arr[offset2] = int(str(new_height)[:2], 16)
    bin_arr[offset2 + 1] = int(str(new_height)[2:], 16)

    logger.info("Saving new image file")
    with open(output, "wb") as binary_file:
        binary_file.write(b"".join([(x).to_bytes(1, "big") for x in bin_arr]))
    logger.info("Image saved!")


def modify_png(filename, output, width, height):
    modify_file(18, 22, filename, output, width, height)

    # Fix crc32 checksum
    logger.info("Fixing checksum of new image")
    call(["pngcsum", "%s" % output, output + "new"])
    logger.info("Checksum now OK")

    os.remove("%s" % output)
    os.rename("%snew" % output, output)


def modify_jpg(filename, output, width, height):
    bin_arr = []
    with open(filename, "rb") as f:
        arr = f.read()
    prev = ""
    i = 0
    for b in arr:
        if prev + hex(b)[2:] == "ffc0":
            break
        i += 1
        prev = hex(b)[2:]
    logger.info("Found magic bytes on offset %d " % i)
    modify_file(i + 6, i + 4, filename, output, width, height)


def process_file(filename, output, width, height):
    kind = filetype.guess(filename)
    if kind is None:
        print("Filetype not supported!")
        return
    if kind.mime == "image/png":
        logger.info("Detected: png")
        modify_png(filename, output, width, height)
    elif kind.mime == "image/jpeg":
        logger.info("Detected: jpg")
        modify_jpg(filename, output, width, height)
    else:
        logger.info("Filetype not supported")


process_file(args.file, args.output, args.width, args.height)
````

---

## Menjalankan Script

Saya mengubah dimensi gambar menjadi:

* Width: `2016`
* Height: `1120`

Command yang digunakan:

```bash
python3 modsize.py --width 2016 --height 1120 abondoned_street_challenge2.jpg outpng.png
```

Setelah file output dibuka (`outpng.png`), bagian gambar yang sebelumnya tersembunyi berhasil terlihat, dan flag muncul pada area tambahan tersebut.

![outpng.png](outpng.png)

---

## Flag

```
urban_exploration
```
