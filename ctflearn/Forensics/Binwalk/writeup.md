# Binwalk

## Deskripsi
Here is a file with another file hidden inside it. Can you extract it? [PurpleThing.jpeg](https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY)

---

## Analisis

Diberikan file gambar `PurpleThing.jpeg`, saat saya lihat metadatanya dengan `exiftool`:

```bash
exiftool PurpleThing.jpeg
```

Outptut:

```
ExifTool Version Number         : 13.25
File Name                       : PurpleThing.jpeg
Directory                       : .
File Size                       : 165 kB
File Modification Date/Time     : 2026:01:06 22:25:15+07:00
File Access Date/Time           : 2026:01:06 22:25:25+07:00
File Inode Change Date/Time     : 2026:01:06 22:25:25+07:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 780
Image Height                    : 720
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 780x720
Megapixels                      : 0.562
```

Meskipun nama file berformat `.jpeg`, `exiftool` mengidentifikasi file tersebut sebagai PNG. Selain itu, terdapat peringatan penting:

```
Warning : [minor] Trailer data after PNG IEND chunk

```

Peringatan ini menunjukkan bahwa terdapat **data tambahan setelah chunk IEND**, yang secara struktur seharusnya menandai akhir file PNG. Kondisi ini sering menjadi indikasi adanya **file lain yang disisipkan (_file embedding_)**.
Berdasarkan temuan tersebut, dilakukan proses ekstraksi menggunakan tool _file carving_ `foremost`:

```bash
foremost PurpleThing.jpeg
```

Hasil ekstraksi menghasilkan beberapa file PNG:

```
00000000.png  00000299.png
```

membuka file `00000299.png` memberi kita flag
![Flag](output/png/00000299.png)

---

## Flag

```ABCTF{b1nw4lk_is_us3ful}```
