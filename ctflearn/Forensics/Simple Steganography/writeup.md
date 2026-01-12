# Simple Steganography

## Challenge Overview

Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"  
[Minions1.jpg](https://ctflearn.com/challenge/download/894)

---

## Analisis Awal

File `Minions1.jpg` dibuka secara visual dan tidak menunjukkan adanya indikasi tersembunyi pada tampilan gambar.

Langkah berikutnya adalah melakukan analisis metadata menggunakan `exiftool` untuk mencari informasi non-visual.

```bash
exiftool Minions1.jpg
```

Dari hasil metadata, ditemukan informasi yang mencurigakan:

```text
Keywords : myadmin
```

Nilai tersebut diduga merupakan **passphrase** untuk proses ekstraksi steganografi.

---

## Ekstraksi Data Tersembunyi

Dengan memanfaatkan hint challenge dan keyword yang ditemukan, dilakukan ekstraksi menggunakan `steghide`:

```bash
steghide extract -sf Minions1.jpg
```

Saat diminta passphrase, digunakan:

```
myadmin
```

Proses ekstraksi berhasil dan menghasilkan file:

```
raw.txt
```

---

## Analisis File Hasil Ekstraksi

Isi dari `raw.txt` diperiksa:

```bash
cat raw.txt
```

Output:

```text
AEMAVABGAGwAZQBhAHIAbgB7AHQAaABpAHMAXwBpAHMAXwBmAHUAbgB9
```

String tersebut teridentifikasi sebagai **Base64 encoding**.

---

## Dekode Base64

Proses decoding dilakukan menggunakan perintah berikut:

```bash
echo 'AEMAVABGAGwAZQBhAHIAbgB7AHQAaABpAHMAXwBpAHMAXwBmAHUAbgB9' | base64 -d
```

Hasil decoding:

```text
CTFlearn{this_is_fun}
```

---

## Flag

```text
CTFlearn{this_is_fun}
```
