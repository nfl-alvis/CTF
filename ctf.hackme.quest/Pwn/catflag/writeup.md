# catflag

## Deskripsi Challenge

`nc ctf.hackme.quest 7709`  
Try using `nc` connect to server!

---

## Analisis

Challenge menyediakan sebuah service remote yang dapat diakses menggunakan `nc`.

Saat terhubung, server memberikan akses shell sederhana. Dengan melakukan listing directory menggunakan `ls`, terlihat file bernama `flag`. Selanjutnya, file tersebut dapat dibaca menggunakan perintah `cat flag` untuk memperoleh flag.

Berikut salah satu contoh interaksi dengan service:

```txt
nc ctf.hackme.quest 7709
plz capture the flag after 5 seconds...
plz capture the flag after 4 seconds...
plz capture the flag after 3 seconds...
plz capture the flag after 2 seconds...
plz capture the flag after 1 seconds...
ls
flag
run.sh
shell
cat flag
FLAG{cat flag? dog flag!}
```

---

## Flag

```FLAG{cat flag? dog flag!}```
