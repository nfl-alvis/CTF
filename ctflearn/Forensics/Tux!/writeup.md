# Tux!

## Challenge Overview

The flag is hidden inside the Penguin! Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.  
[Tux.jpg](https://ctflearn.com/challenge/download/973)

---

## Analisis

Diberikan sebuah file gambar bernama `Tux.jpg`.  
  
![Tux.jpg](Tux.jpg)  
  
Langkah awal adalah memeriksa **metadata** gambar untuk mencari informasi tersembunyi. Dari hasil analisis metadata, ditemukan sebuah string **Base64** pada bagian *Comment*:

```
Comment : ICAgICAgUGFzc3dvcmQ6IExpbnV4MTIzNDUK
```

---

## Decode Metadata

String Base64 tersebut didekode dan menghasilkan plaintext berikut:

```
Password: Linux12345
```

Pada tahap ini belum jelas password tersebut digunakan untuk apa, sehingga diperlukan analisis lanjutan terhadap struktur file gambar.

---

## Ekstraksi File Tersembunyi

Selanjutnya dilakukan analisis dengan **binwalk** untuk mendeteksi adanya file yang ter-embed di dalam gambar:

```bash
binwalk -e Tux.jpg
```

Hasilnya menunjukkan adanya sebuah arsip ZIP terenkripsi:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
5488          0x1570          Zip archive data, encrypted at least v1.0 to extract,
                             compressed size: 39, uncompressed size: 27, name: flag
```

Ini mengindikasikan bahwa file gambar mengandung **ZIP archive tersembunyi** yang dilindungi oleh password.

---

## Ekstraksi ZIP dan Flag

ZIP hasil ekstraksi kemudian dibuka. Saat diminta password, digunakan password yang diperoleh dari metadata sebelumnya:

```
Password: Linux12345
```

Proses ekstraksi berhasil dan menghasilkan sebuah file bernama `flag`.

Untuk membaca isinya:

```bash
cat flag
```

Output:

```
CTFlearn{Linux_Is_Awesome}
```

---

## Flag

```text
CTFlearn{Linux_Is_Awesome}
```
