# Character Encoding

## Deskripsi

In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D

---

## Analisis

Diberikan sebuah deretan nilai dalam format _**hexadecimal**_:

```
41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D
```

Nilai-nilai tersebut menyerupai representasi **ASCII** yang telah dikonversi ke bentuk _*hexadecimal*_.

---

## Decode

Untuk mendekode data tersebut, digunakan perintah `xxd` dengan opsi `-r -p` yang berfungsi untuk mengubah input hexadecimal menjadi representasi karakter **ASCII**.

```bash
echo '41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D' | xxd -r -p
```

Output:

```
ABCTF{45C11_15_U53FUL}
```

---

## Flag

```ABCTF{45C11_15_U53FUL}```
