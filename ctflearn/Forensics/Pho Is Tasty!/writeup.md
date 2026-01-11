# Pho Is Tasty!

---

## Challenge

The flag is hidden in the jpeg file. Good Luck! Have some Pho! Solve this challenge before solving my Scope challenge for 100 points.  
[Pho.jpg](https://ctflearn.com/challenge/download/971)

---

## Analisis Awal

Gambar `Pho.jpg` dibuka secara normal dan tidak menunjukkan anomali visual.  
  
![Pho.jpg](Pho.jpg)
Langkah selanjutnya adalah melakukan **analisis level byte** untuk mencari kemungkinan string tersembunyi di dalam struktur file.

---

## Investigasi Biner

Dilakukan pemeriksaan menggunakan `hexdump` untuk melihat representasi heksadesimal dan ASCII dari file:

```bash
hexdump -C Pho.jpg | head
```

Output awal menunjukkan header JPEG yang valid (`JFIF`) serta metadata kamera.
Namun, pada bagian awal file ditemukan **karakter ASCII yang membentuk pola mencurigakan**, meskipun diselingi byte non-printable (`.`).

Contoh potongan hasil dump:

```
|..C..T..F..l..e.|
|.a..r..n..{..I.|
|_..L..o..v..e._|
|..P..h..o..!..!|
|.!..}|
```

---

## Ekstraksi Flag

Karena karakter flag terpisah oleh byte non-ASCII, perintah `strings` tidak berhasil mendeteksinya.
Untuk mengatasinya, karakter titik (`.`) pada output ASCII dihapus menggunakan `sed`, lalu dilakukan pencarian string `CTF`.

```bash
hexdump -C Pho.jpg | sed "s/[.]//g" | grep "CTF" -A 4
```

Hasilnya menunjukkan potongan ASCII yang jika digabungkan membentuk flag lengkap:

```
CTFlearn{I_Love_Pho!!!}
```

---

## Flag

```text
CTFlearn{I_Love_Pho!!!}
```
