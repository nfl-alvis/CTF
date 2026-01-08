# I'm a dump

---

## Deskripsi

The keyword is hexadecimal, and removing an useless H.E.H.U.H.E. from the flag. The flag is in the format CTFlearn{*}

---

## Analisis

Karena berkas yang diberikan merupakan file ELF, pendekatan yang paling tepat adalah melakukan **dump heksadesimal** untuk mencari string yang mengandung pola `CTFlearn`.
Sesuai petunjuk, karakter `H`, `E`, dan `U` dianggap sebagai noise dan perlu dihapus dari hasil ekstraksi.

---

## Proses Ekstraksi

Perintah yang digunakan:

```bash
hexdump -C 883 | grep -A 2 "CTFlearn" | sed "s/[E.HU]//g"
```

1. `hexdump -C 883` Melakukan _hexdump_ terhadap file ELF.
2. `grep -A 2 "CTFlearn"` Mencari baris yang mengandung string `CTFlearn`.
3. `sed "s/[E.HU]//g"` Menghapus karakter _noise_ sesuai petunjuk.

Output:

```
00001150  48 b8 43 54 46 6c 65 61  72 6e 48 ba 7b 66 6c 34  |CTFlearn{fl4|
00001160  67 67 79 66 48 89 45 d0  48 89 55 d8 48 c7 45 e0  |ggyf|
00001170  6c 34 67 7d 48 c7 45 e8  00 00 00 00 48 c7 45 f0  |l4g}|
```

Jika bagian ASCII dari dump tersebut digabungkan, akan membentuk string _flag_ yang lengkap.

---

## Flag

```CTFlearn{fl4ggyfl4g}```
