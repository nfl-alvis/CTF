# My Friend John

## Challenge

Have you met my friend John?  
He's not so scary, even though they call him "The Ripper".  
[MyFriendJohn.zip](https://ctflearn.com/challenge/download/1135)

---

## Analisis

Challenge ini mengindikasikan penggunaan **John The Ripper** sebagai metode utama, diperkuat dengan petunjuk julukan *"The Ripper"* serta nama file `use-rockyou.zip`.

Langkah pertama adalah mengekstrak arsip utama:

```bash
unzip MyFriendJohn.zip
```

Output:

```
Archive:  MyFriendJohn.zip
 extracting: use-rockyou.zip
```

File `use-rockyou.zip` ternyata **terproteksi password**, sehingga diperlukan proses cracking.

---

## Tahap 1 — Cracking `use-rockyou.zip`

Generate hash zip:

```bash
zip2john use-rockyou.zip > use-rockyou.hash
```

Crack menggunakan John:

```bash
john use-rockyou.hash
```

Output:

```
kdbs0429 (use-rockyou.zip)
```

Ekstraksi arsip:

```bash
unzip use-rockyou.zip
```

Output:

```
inflating: custom-list.txt
extracting: custom-list.zip
```

Didapatkan:

* `custom-list.txt` → Wordlist khusus
* `custom-list.zip` → Arsip berpassword

---

## Tahap 2 — Cracking `custom-list.zip`

Generate hash:

```bash
zip2john custom-list.zip > custom-list.hash
```

Crack menggunakan wordlist yang disediakan:

```bash
john --wordlist=custom-list.txt custom-list.hash
```

Output:

```
1N73rD3N0M1N4710N41 (custom-list.zip/brute-force-pin.zip)
```

Ekstraksi arsip:

```bash
unzip custom-list.zip
```

Output:

```
extracting: brute-force-pin.zip
```

---

## Tahap 3 — Cracking `brute-force-pin.zip`

Generate hash:

```bash
zip2john brute-force-pin.zip > brute-force-pin.hash
```

Crack dengan wordlist rockyou:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt brute-force-pin.hash
```

Output:

```
991337 (brute-force-pin.zip/flag.txt)
```

Ekstraksi arsip terakhir:

```bash
unzip brute-force-pin.zip
```

Output:

```
extracting: flag.txt
```

---

## Flag

```
CTFlearn{s0_n0W_y0uv3_M3t_J0hN}
```
