# Milk's Best Friend

---

## Deskripsi 

There's nothing I love more than oreos, lions, and winning. 
[oreo.jpg](https://mega.nz/#!DC5F2KgR!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y)
Have Fun :)

---

## Analisis

Diberikan sebuah gambar `oreo.jpg`:  
  
![oreo.jpg](oreo.jpg)
  
Langkah awal yang dilakukan adalah memeriksa kemungkinan adanya file tersembunyi di dalam gambar menggunakan `binwalk`.

```bash
binwalk -e oreo.jpg
```

Perintah tersebut berhasil mengekstrak beberapa file yang ter-_embed_ di dalam gambar:

```
.
├── 252B.rar
├── a
└── b.jpg
```

Hasil ini mengindikasikan bahwa `oreo.jpg` bukan hanya berisi data gambar, tetapi juga mengandung beberapa file tambahan.

---

## Pencarian Flag

Selanjutnya dilakukan pencarian _string_ yang mengandung kata _flag_ pada seluruh file hasil ekstraksi menggunakan _command_ `strings` dan `grep`.

```bash
strings * | grep flag
```

Output:

```
This is not the flag you are looking for.Q"t
This is not the flag you are looking for.
Finally, flag{eat_more_oreos}
```

Dua baris pertama merupakan _decoy_, sedangkan baris terakhir mengandung _flag_ yang valid.

---

## Flag 

```flag{eat_more_oreos}```
