# television

## Deskripsi Challenge

Looks like my television was broken

---

## Analisis

Diberikan sebuah file gambar bernama `television.bmp`.  
  
![television.bmp](television.bmp)  
  
Langkah awal yang dilakukan adalah melakukan ekstraksi string yang mungkin tersimpan di dalam file menggunakan `strings`, lalu memfilter hasilnya dengan `grep` untuk mencari kata kunci `FLAG`.

```bash
strings television.bmp | grep FLAG
```

Dari command tersebut, ditemukan flag berikut:

```FLAG{PuRe_R@ND0M_DaTa_Fr0M/D3V/UR@ND0M}```

---

## Flag

```FLAG{PuRe_R@ND0M_DaTa_Fr0M/D3V/UR@ND0M}```
