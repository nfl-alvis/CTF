# Minions

## Challenge Overview

Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there:  
[Hey_You.png](https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg) Can you help me?  
TIP: Decode the flag until you got a sentence.

---

## Analisis & Eksploitasi

### 1. Analisis Awal File `Hey_You.png`

File `Hey_You.png` dibuka secara visual dan tidak menunjukkan indikasi mencurigakan:

![Hey\_You.png](Hey_You.png)

Karena tidak ada petunjuk visual, langkah selanjutnya adalah mencari **data tersembunyi (embedded plaintext)** menggunakan perintah `strings`.

```bash
strings Hey_You.png
```

Dari output tersebut ditemukan sebuah URL mencurigakan:

```
https://mega.nz/file/wZw2nAhS#i3Q0r-R8psiB8zwUrqHTr661d8FiAS1Ott8badDnZkoH
```

---

### 2. File Kedua: `Only_Few_Steps.jpg`

URL tersebut mengarah ke unduhan file gambar bernama `Only_Few_Steps.jpg`.

![Only\_Few\_Steps.jpg](Only_Few_Steps.jpg)

Secara visual, gambar ini juga tidak mengandung informasi mencurigakan. Kembali dilakukan analisis menggunakan `strings`.

```bash
strings Only_Few_Steps.jpg
```

Dari hasil output ditemukan nama file lain:

```
YouWon(Almost).jpg
```

Hal ini mengindikasikan adanya **file lain yang di-embed** di dalam `Only_Few_Steps.jpg`.

---

### 3. Ekstraksi File Tersembunyi

Untuk mengekstrak file yang tertanam, digunakan tool `binwalk`.

```bash
binwalk -e Only_Few_Steps.jpg
```

Hasil ekstraksi menghasilkan struktur folder berikut:

```
_Only_Few_Steps.jpg.extracted
├── 22806.rar
└── YouWon(Almost).jpg
```

File yang relevan untuk analisis selanjutnya adalah `YouWon(Almost).jpg`.

---

### 4. Analisis `YouWon(Almost).jpg`

File `YouWon(Almost).jpg` tidak menunjukkan petunjuk visual yang mencurigakan:

![YouWon(Almost).jpg](_Only_Few_Steps.jpg.extracted/YouWon\(Almost\).jpg)

Dilanjutkan dengan analisis `strings` untuk mencari plaintext tersembunyi.

```bash
strings YouWon\(Almost\).jpg | head
```

Ditemukan string dengan format flag yang isinya masih terenkripsi:

```
CTF{VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=}
```

---

### 5. Proses Decoding

Isi flag tersebut terlihat menggunakan **Base64 encoding**.
Dilakukan decoding Base64 secara berulang hingga diperoleh plaintext yang dapat dibaca.

Hasil akhir decoding:

```
M1NI0NS_ARE_C00L
```

---

## Flag

```text
CTF{M1NI0NS_ARE_C00L}
```
