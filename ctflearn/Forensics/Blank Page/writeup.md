# Blank Page

## Challenge

I've just graduated the Super Agent School. This is my first day as a spy. The Master-Mind sent me the secret message, but I don't remember how to read this. Help!  
[TheMessage.txt](TheMessage.txt)

---

## Analysis

Diberikan sebuah file teks bernama `TheMessage.txt`. Ketika file tersebut dibaca menggunakan perintah standar seperti:

```bash
cat TheMessage.txt
```

tidak ada output yang ditampilkan, seolah-olah file tersebut kosong. Hal ini mengindikasikan kemungkinan penggunaan **karakter tak terlihat (invisible characters)**.

Untuk menyelidiki lebih lanjut, isi file dianalisis pada level byte menggunakan `xxd`:

```bash
xxd TheMessage.txt | head -20
```

Hasilnya menunjukkan pola byte yang berulang, khususnya:

```
20 e2 80 8f
```

* `0x20` → karakter spasi ASCII
* `0xE2 0x80 0x8F` → **Unicode Right-to-Left Mark (RLM)**, karakter tak terlihat

Dari pola ini dapat disimpulkan bahwa pesan disembunyikan menggunakan **dua jenis karakter berbeda namun sama-sama tidak terlihat secara visual**, yang lazim digunakan untuk menyandikan data biner.

### Asumsi Encoding

* Spasi (`0x20`) direpresentasikan sebagai **0**
* Karakter Unicode tak terlihat (`0xE2808F`) direpresentasikan sebagai **1**

Dengan asumsi tersebut, seluruh isi file dapat diekstraksi menjadi sebuah bitstream, kemudian dikelompokkan per 8 bit (1 byte) dan dikonversi ke karakter ASCII.

---

## Decoding

Untuk melakukan ekstraksi dan decoding, digunakan script Python berikut:

```python
data = open("TheMessage.txt", "r").read()

bits = ""
for char in data:
    if ord(char) == 32:
        bits += "0"
    else:
        bits += "1"

decoded = ""
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) == 8:
        decoded += chr(int(byte, 2))

print("=== BITSTREAM ===")
print(bits)
print("\n=== DECODED TEXT ===")
print(decoded)
```

---

## Result

Menjalankan script tersebut menghasilkan teks terdekripsi sebagai berikut:

```
From The Global Anti-Terrorists Tactics

If you read this you passed. Congrats.
Your first task will come tomorrow.
Good luck.

CTFlearn{If_y0u_r3/\d_thi5_you_pa553d}
```

Pesan tersembunyi berhasil direkonstruksi sepenuhnya, dan flag ditemukan pada bagian akhir pesan.

---

## Flag

```text
CTFlearn{If_y0u_r3/\d_thi5_you_pa553d}
```
