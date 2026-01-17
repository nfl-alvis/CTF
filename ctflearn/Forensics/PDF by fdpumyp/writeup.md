# PDF by fdpumyp

## Challenge Overview

Hi, just as we talked during a break, you have this file here and check if something is wrong with it. That's the only thing we found strange with this suspect, I hope there will be a password for his external drive  
  
Bye  
  
[dontopen.pdf](https://ctflearn.com/challenge/download/957)

---

## Analisis

### 1. Pemeriksaan Awal File

File `dontopen.pdf` dibuka secara statis tanpa menjalankannya.
Untuk mencari kemungkinan **data tersembunyi dalam bentuk plaintext**, dilakukan analisis menggunakan perintah `strings`.

```bash
strings dontopen.pdf
```

---

### 2. Menemukan Informasi Mencurigakan

Dari hasil perintah `strings`, ditemukan beberapa baris yang jelas tidak lazim untuk sebuah file PDF biasa:

```text
== SECRET DATA DONT LOOK AT THIS ==
external:Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==
pin:1234
password:MTIzMVdST05HOWlzamRuUEFTU1dPUkQ=
```

Terlihat bahwa:

* Terdapat beberapa field sensitif (`external`, `pin`, `password`)
* Nilai pada field `external` dan `password` tampak menggunakan **Base64 encoding**

---

### 3. Decoding Base64

Fokus utama adalah field `external`, karena mengandung pola flag CTF.

Dilakukan decoding Base64 menggunakan perintah berikut:

```bash
echo 'Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==' | base64 -d
```

Hasil decoding:

```text
CTFlearn{)_1l0w3y0Um00my123}
```

---

## Flag

```text
CTFlearn{)_1l0w3y0Um00my123}
```
