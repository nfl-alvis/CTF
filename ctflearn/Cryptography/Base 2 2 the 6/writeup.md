# Base 2 2 the 6

# Deskripsi

There are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9

---

## Analisis

Diberikan sebuah _string_

```
Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9
```

Berdasarkan struktur string yang terdiri dari karakter alfanumerik (`A–Z`, `a–z`, `0–9`) tanpa karakter non-standar, dapat diasumsikan bahwa data tersebut di encode dengan **Base64 encoding**.

---

## Proses Decode

Proses decoding dilakukan menggunakan perintah `base64` dengan opsi `-d` yaitu untuk mendecode.

```bash
echo 'Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9' | base64 -d
```

Output:

```
CTF{FlaggyWaggyRaggy}
```

---

## Flag 

```CTF{FlaggyWaggyRaggy}```
