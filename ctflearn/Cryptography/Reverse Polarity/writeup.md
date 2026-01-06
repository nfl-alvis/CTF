# Reverse Polarity

## Deskripsi

I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101

---

## Analisis 

Diberikan data yang berupa rangkaian angka `0` dan `1` tanpa pemisah, yang mengindikasikan representasi biner **ASCII 8-bit**.
Panjang data merupakan kelipatan 8, sehingga dapat diasumsikan bahwa setiap 8 bit merepresentasikan satu karakter ASCII.

```
01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101
```

---

## Proses Decode

Proses dekode dilakukan dengan mengonversi _binary string_ langsung ke karakter ASCII menggunakan utilitas `perl`.

```bash
echo 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101 | perl -lpe '$_=pack("B*",$_)'
```

Output:

```
CTF{Bit_Flippin}
```

---

## Flag

```CTF{Bit_Flippin}```
