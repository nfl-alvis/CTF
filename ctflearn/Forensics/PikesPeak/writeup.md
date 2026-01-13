# PikesPeak

## Challenge Overview

Pay attention to those strings!
[PikesPeak.jpg](https://ctflearn.com/challenge/download/935)

---

## Analisis

File `PikesPeak.jpg` dibuka secara visual dan tidak menampilkan indikasi steganografi secara kasat mata.  
  
![PikesPeak.jpg](PikesPeak.jpg)  
  
Berdasarkan hint challenge, dilakukan ekstraksi string ASCII yang tertanam di dalam file menggunakan perintah `strings`.

```bash
strings PikesPeak.jpg
```

Dari hasil eksekusi perintah tersebut, ditemukan beberapa kandidat flag:

```
CTFLEARN{PikesPeak}
CTFLearn{Colorado}
%ctflearn{MountainMountainMountain}
\#cTfLeArN{CTFMountainCTFmOUNTAIN}
CTF{AsPEN.Vail}
CTFlearn{Gandalf}
ctflearning{AUCKLAND}
ctfLEARN{MtDoom}
6ctflearninglearning{Mordor.TongariroAlpineCrossing}
+CTFLEARN{MountGedePangrangoNationalPark}
$ctflearncTfLeARN{MountKosciuszko}
```

---

## Validasi Flag

Berdasarkan standar format flag pada platform **CTFlearn**, flag yang valid harus mengikuti format:

```
CTFlearn{...}
```

Dari seluruh kandidat yang ditemukan, hanya satu string yang **sepenuhnya sesuai dengan format flag resmi** tanpa karakter tambahan atau kesalahan kapitalisasi.

---

## Flag

```text
CTFlearn{Gandalf}
```
