# snow

![challenge.png](challenge.png)

---

## Deskripsi Challenge

Pada challenge ini, diberikan dua buah file:

* `note.txt`
* `snow.jpg`

Isi dari `note.txt` sekilas terlihat normal, namun terdapat kejanggalan berupa banyak baris kosong dan kemungkinan penggunaan spasi tersembunyi:

```
Salju menutupi banyak hal, tapi bukan semuanya hilang.
Perhatikan foto musim dingin — mungkin ada sesuatu yang tersembunyi di balik lapisan putih.
pass: snowflake
```

Selain itu, diberikan file gambar `snow.jpg` yang secara visual tidak menunjukkan indikasi manipulasi atau artefak mencurigakan.

![snow.jpg](snow.jpg)

---

## Langkah Penyelesaian

### 1. Analisis Awal

Petunjuk pada deskripsi teks seperti:

> “Salju menutupi banyak hal...”
> “...sesuatu yang tersembunyi di balik lapisan putih.”

mengindikasikan kemungkinan penggunaan teknik **steganografi**.

Keberadaan banyak spasi dan baris kosong pada `note.txt` mengarah pada dugaan penggunaan metode *whitespace steganography*, khususnya tools **StegSnow** yang menyembunyikan data dalam karakter spasi dan tab di akhir baris.

Selain itu, terdapat kata `pass: snowflake` yang diduga sebagai passphrase untuk proses ekstraksi.

---

### 2. Ekstraksi Data dari `note.txt`

Dilakukan proses ekstraksi menggunakan `stegsnow` dengan passphrase yang tersedia:

```bash
stegsnow -p snowflake -C note.txt
```

Output yang diperoleh:

```
frozzen_99_❄️⛄
```

String hasil ekstraksi tersebut terlihat seperti sebuah passphrase lanjutan. Hal ini memperkuat dugaan bahwa challenge ini menggunakan steganografi berlapis (*multi-layer steganography*).

---

### 3. Ekstraksi Data dari `snow.jpg`

Passphrase hasil tahap sebelumnya kemudian digunakan untuk mengekstrak data dari file gambar menggunakan `steghide`:

```bash
steghide extract -sf snow.jpg -p "frozzen_99_❄️⛄"
```

Output:

```
wrote extracted data to "flag.txt".
```

File `flag.txt` berhasil diekstrak.

---

### 4. Analisis Isi `flag.txt`

Isi dari `flag.txt` berupa rangkaian emoji salju dan manusia salju:

```
❄⛄❄❄❄⛄⛄❄❄⛄❄❄⛄⛄❄❄❄⛄❄❄❄❄❄⛄❄⛄❄❄❄⛄⛄⛄❄⛄⛄⛄⛄❄⛄⛄❄⛄⛄⛄❄⛄⛄⛄❄⛄⛄❄⛄❄❄⛄❄⛄⛄❄⛄⛄⛄❄❄⛄⛄⛄❄⛄❄❄❄⛄⛄❄❄⛄❄⛄❄⛄⛄⛄❄❄⛄❄❄⛄❄⛄⛄⛄⛄⛄❄⛄⛄❄⛄❄❄⛄❄⛄⛄⛄❄❄⛄⛄❄⛄❄⛄⛄⛄⛄⛄❄⛄⛄❄⛄❄❄❄❄⛄⛄❄❄⛄❄⛄❄⛄⛄⛄❄❄⛄❄❄⛄⛄❄❄⛄❄⛄❄⛄❄⛄⛄⛄⛄⛄❄❄⛄⛄❄❄⛄❄❄❄⛄⛄❄❄❄❄❄❄⛄⛄❄❄⛄❄❄❄⛄⛄❄⛄❄⛄❄⛄⛄⛄⛄⛄❄⛄
```

Pada tahap ini, terlihat bahwa karakter yang digunakan hanya dua jenis:

* ❄  (snowflake)
* ⛄ (snowman)

Karena hanya terdapat dua simbol berbeda, besar kemungkinan ini merupakan representasi biner.

---

### 5. Proses Decoding

Dilakukan pemetaan sebagai berikut:

```
❄️ = 0
⛄ = 1
```

Setelah seluruh simbol dikonversi ke bentuk biner, hasilnya dikelompokkan per 8 bit dan dikonversi ke representasi ASCII.

Proses decoding menghasilkan sebuah string yang merupakan flag dengan format FLAG{.

Setelah disesuaikan dengan format flag yang digunakan pada kompetisi (FGTE), diperoleh flag final yang valid.

![solved.png](solvef.png)

---

## Flag

```
FGTE{Redacted}
```
