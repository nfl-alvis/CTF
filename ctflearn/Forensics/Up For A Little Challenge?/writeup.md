# Up For A Little Challenge

---

## Challenge

[Begin Hack.jpg](https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0)  
You Know What To Do ...

---

## Analisis Awal

File `Begin Hack.jpg` dibuka secara normal dan tidak menunjukkan indikasi visual yang mencurigakan.  
  
![Begin Hack.jpg](chall/Begin%20Hack.jpg)  
  
Langkah pertama adalah melakukan **string analysis** untuk mencari informasi tersembunyi di dalam struktur file.

```bash
strings "Begin Hack.jpg"
```

Dari hasil tersebut ditemukan dua informasi penting:

```text
real_unlock_key: Nothing Is As It Seems
https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg
```

* Sebuah **unlock key**
* Sebuah **link Mega** yang mengarah ke file lanjutan

---

## Ekstraksi Arsip Lanjutan

Link Mega mengarah ke file arsip:

```
Up For A Little Challenge.zip
```

Setelah diekstrak, struktur direktori yang diperoleh adalah:

```
.
├── Did I Forget Again?
│   ├── Loo Nothing Becomes Useless ack.jpg
│   └── .Processing.cerb4
└── __MACOSX (Metadata)
    ├── ._Did I Forget Again?
    └── Did I Forget Again?
        ├── ._Loo Nothing Becomes Useless ack.jpg
        └── ._.Processing.cerb4
```

Fokus utama tertuju pada file tersembunyi:

```
.Processing.cerb4
```

---

## Analisis File Tersembunyi

Pemeriksaan tipe file dilakukan menggunakan perintah `file`:

```bash
file "Did I Forget Again?/.Processing.cerb4"
```

Output:

```
Zip archive data, made by v3.0 UNIX, extract using at least v2.0
```

File tersebut ternyata merupakan **ZIP archive yang disamarkan** dengan ekstensi tidak umum.

---

## Dekripsi Arsip

Saat diekstrak, arsip meminta password.
Unlock key yang sebelumnya ditemukan digunakan sebagai password:

```
Nothing Is As It Seems
```

Proses ekstraksi berhasil dan menghasilkan file baru:

```
skycoder.jpg
```

---

## Penemuan Flag

File `skycoder.jpg` dibuka secara visual.  
  
![skycoder.jpg](chall/skycoder.jpg)  
  
Dengan memperhatikan gambar secara detail, terlihat **teks berwarna merah di pojok kanan bawah gambar** yang berisi flag challenge.

---

## Flag

```text
flag{hack_complete}
```
