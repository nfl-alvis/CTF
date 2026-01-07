# 07601

---

## Deskripsi

I think I lost my flag in there. Hopefully, it won't get attacked...
[AGT.png](https://mega.nz/#!CXYXBQAK!6eLJSXvAfGnemqWpNbLQtOHBvtkCzA7-zycVjhHPYQQ)

---

## Analisis 

Diberikan file gambar `AGT.png`:  
![AGT.png](chall/AGT.png)

File `AGT.png` tampak sebagai file gambar biasa. Namun, untuk memastikan format sebenarnya, dilakukan identifikasi tipe berkas menggunakan perintah file.

```bash
file AGT.png
```

Output:

```
AGT.png: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 300x168, components 3
```

Dari hasil tersebut diketahui bahwa meskipun berekstensi `.png`, berkas ini sebenarnya berformat **JPEG**. Oleh karena itu, ekstensi file disesuaikan agar konsisten dengan format sebenarnya.

```bash
cp AGT.png AGT.jpeg
```

---

## Analisis Hexadecimal

Langkah selanjutnya adalah menganalisis isi berkas pada level heksadesimal untuk mencari indikasi adanya data tersembunyi.

```bash
xxd AGT.jpeg | tail
```

Output:

```
0006a570: 2f55 5808 002c fc15 582c fc15 5850 4b01  /UX..,..X,..XPK.
0006a580: 0215 0314 0008 0008 0009 4f5e 4970 1a8d  ..........O^Ip..
0006a590: c05d 0000 00ab 0000 003f 000c 0000 0000  .].......?......
0006a5a0: 0000 0000 4080 8137 2502 005f 5f4d 4143  ....@..7%..__MAC
0006a5b0: 4f53 582f 5365 6372 6574 2053 7475 6666  OSX/Secret Stuff
0006a5c0: 2e2e 2e2f 446f 6e27 7420 4f70 656e 2054  .../Don't Open T
0006a5d0: 6869 732e 2e2e 2f2e 5f49 2057 6172 6e65  his.../._I Warne
0006a5e0: 6420 596f 752e 6a70 6567 5558 0800 03fc  d You.jpegUX....
0006a5f0: 1558 02fc 1558 504b 0506 0000 0000 0900  .X...XPK........
0006a600: 0900 4303 0000 1126 0200 0000            ..C....&....
```

Output menunjukkan adanya _signature_ mencurigakan, seperti `PK` yang merupakan _signature_ file **_ZIP Archive_**, dan terlihat juga path seperti `__MACOSX/Secret Stuff...`
Hal ini mengindikasikan bahwa terdapat beberapa file yang di-_embed_ di dalam gambar.

---

## Ekstraksi Berkas Tersembunyi

Untuk mengekstrak file tersembunyi tersebut, digunakan `binwalk`:

```bash
binwalk -e AGT.jpeg
```

Hasil ekstraksi menghasilkan struktur berkas sebagai berikut:

```
.
├── 25118.zip
├── 2570.zip
├── 47CA2.zip
├── I Warned You.jpeg
├── __MACOSX
│   └── Secret Stuff...
│       └── Don't Open This...
└── Secret Stuff...
    └── Don't Open This...
        └── I Warned You.jpeg
```

## Pencarian Flag

Salah satu file hasil ekstraksi adalah gambar `I Warned You.jpeg`. Untuk mencari kemungkinan _flag_ tersembunyi di dalamnya, dilakukan pencarian string menggunakan `strings`.

```bash
strings "I Warned You.jpeg" | grep -i "CTF"
```

Output:

```
ABCTF{Du$t1nS_D0jo}
```

---

## Flag

```ABCTF{Du$t1nS_D0jo}```
