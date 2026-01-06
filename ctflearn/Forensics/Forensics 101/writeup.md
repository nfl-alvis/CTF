# Forensics 101

## Deskripsi

Think the flag is somewhere in there. Would you help me find it?
[Chall.jpg](https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c)

---

## Analisis

Diberikan file gambar `Chall.jpg`, meskipun berformat gambar, file ini kemungkinan mengandung string **ASCII tersembunyi** yang dapat diekstrak.

![Chall.jpg](Chall.jpg)

Untuk melakukan analisis awal, digunakan perintah `strings` yang dipipe dengan `grep` untuk mencari kata flag.

```bash
strings Chall.jpg | grep flag
```

Output:

```
flag{wow!_data_is_cool}
```

Dari hasil tersebut dapat disimpulkan bahwa flag tersimpan secara plaintext di dalam file gambar.

---

## Flag

```flag{wow!_data_is_cool}```
