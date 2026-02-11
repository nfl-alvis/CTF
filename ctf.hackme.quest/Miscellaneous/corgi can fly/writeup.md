# Corgi Can Fly

## Deskripsi Challenge

Corgi is cute, right?  
  
[Pillow (Python)](https://pillow.readthedocs.io/) and [Bitmap (.NET)](<https://msdn.microsoft.com/zh-tw/library/system.drawing.bitmap(v=vs.110).aspx>) are your friends.  
  
(Maybe you can try `stegsolve`)


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
