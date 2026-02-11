# Corgi Can Fly

## Deskripsi Challenge

Corgi itu lucu, kan?

Challenge ini dapat diselesaikan menggunakan bantuan library:

- [Pillow (Python)](https://pillow.readthedocs.io/)
- [Bitmap (.NET)](<https://msdn.microsoft.com/zh-tw/library/system.drawing.bitmap(v=vs.110).aspx>)

Selain itu, tools seperti `stegsolve` juga sangat membantu untuk analisis cepat.

---

## Analisis

Diberikan sebuah file gambar bernama:

- `corgi-can-fly.png`

![corgi-can-fly.png](corgi-can-fly.png)

Langkah pertama adalah melakukan inspeksi menggunakan **StegSolve** untuk mencari kemungkinan hidden data pada channel warna.

Saat membuka gambar menggunakan `stegsolve`, ditemukan sebuah QR Code tersembunyi pada menu:

- **Red Plane 0**

![solved.png](solved.png)

QR Code tersebut kemudian dipindai untuk memperoleh flag.

---

## Flag

`FLAG{Corgi is cutest aniaml on the earth >////////<}`
