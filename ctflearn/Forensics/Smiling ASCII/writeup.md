# Smiling ASCII

## Deskripsi Challenge

Find the flag on the smiling face.  
[smiling.png](https://ctflearn.com/challenge/download/903)

---

## Analisis Awal

File `smiling.png` dibuka secara visual untuk inspeksi awal. Tidak ditemukan kejanggalan visual seperti teks tersembunyi, perbedaan warna mencolok, atau artefak yang mencurigakan.  
  
![smiling.png](smiling.png)  
  
Karena tidak ada petunjuk secara kasat mata, kemungkinan besar informasi disembunyikan menggunakan teknik **steganografi non-visual**.

---

## Analisis Data Tersembunyi dengan Zsteg

Langkah selanjutnya adalah memeriksa struktur internal gambar menggunakan **zsteg**, sebuah tool yang umum digunakan untuk mendeteksi data tersembunyi dalam file PNG.

```bash
zsteg smiling.png
```

### Hasil Output

```
[?] 104 bytes of extra data after image end (IEND), offset = 0xe6cd
extradata:0         .. text: "RGlkIHlvdSBrbm93IHRoYXQgcGl4ZWxzIGFyZSwgbGlrZSB0aGUgYXNjaWkgdGFibGUsIG51bWJlcmVkIGZyb20gMCB0byAyNTU/Cg=="
```

Terlihat adanya **data tambahan setelah chunk IEND**, yang berisi sebuah string yang terenkode menggunakan **Base64**.

---

## Decode Base64

String Base64 tersebut didekode menggunakan perintah berikut:

```bash
echo 'RGlkIHlvdSBrbm93IHRoYXQgcGl4ZWxzIGFyZSwgbGlrZSB0aGUgYXNjaWkgdGFibGUsIG51bWJlcmVkIGZyb20gMCB0byAyNTU/Cg==' | base64 -d
```

Hasil Decode :

```
Did you know that pixels are, like the ascii table, numbered from 0 to 255?
```

Pesan ini berfungsi sebagai **hint** , yang mengisyaratkan bahwa nilai piksel (0–255) dapat langsung dipetakan ke karakter ASCII. Artinya, payload kemungkinan **tidak menggunakan teknik LSB klasik**, melainkan memanfaatkan nilai piksel secara langsung sebagai representasi karakter.

---

## Pemindaian Lanjutan

Karena flag belum ditemukan pada pemindaian awal, dilakukan pemindaian menyeluruh menggunakan opsi `--all` pada zsteg.

```bash
zsteg --all smiling.png
```

### Hasil Relevan

```
b8,g,lsb,yx         .. text: "CTFlearn{ascii_pixel_flag}"
b8,a,lsb,yx         .. text: "CTFlearn{ascii_pixel_flag}"
```

Pada channel **Green** dan **Alpha**, dengan konfigurasi `b8` (8-bit), ditemukan string plaintext yang secara jelas merupakan flag.

---

## Flag

```text
CTFlearn{ascii_pixel_flag}
```
