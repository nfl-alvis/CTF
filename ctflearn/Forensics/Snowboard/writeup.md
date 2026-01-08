# Snowboard

---

## Deskripsi

Find the flag in the jpeg file. Good Luck!  
[Snowboard.jpg](https://ctflearn.com/challenge/download/934)

---

## Analisis

Diberikan sebuah gambar `Snowboard.jpg`.  
  
![Snowboard.jpg](Snowboard.jpg)
  
Langkah awal yang dilakukan adalah melakukan pencarian _plaintext_ yang mungkin tersembunyi di dalam file menggunakan utilitas `strings`.

```bash
strings Snowboard.jpg | grep CTF
```

Output:

```
CTFlearn{CTFIsEasy!!!}
```

Hasil tersebut terlihat seperti _flag_, namun setelah saya input flag ternyata salah dan ini hanya **decoy _flag_**.

---

## Analisis Heksadesimal

Selanjutnya dilakukan pemeriksaan heksadesimal terhadap file untuk mencari pola data mencurigakan, dan ditemukan string yang menyerupai **Base64**.

```bash
xxd Snowboard.jpg | head |  awk '{print $NF}'
```

Output:

```
......JFIF.....,
.,......CTFlearn
{CTFIsEasy!!!}..
...Q1RGbGVhcm57U
2tpQmFuZmZ9Cg==.
..#.Exif..II*...
............n...
........t.......
................
....(...........
```

Terlihat adanya string:

```
Q1RGbGVhcm57U2tpQmFuZmZ9Cg==
```

Pola tersebut sangat khas sebagai _**Base64** encoding_.

---

## Decode Base64

String Base64 tersebut kemudian didekodekan menggunakan perintah berikut:

```bash
echo "Q1RGbGVhcm57U2tpQmFuZmZ9Cg==" | base64 -d
```

Hasil dekode:

```
CTFlearn{SkiBanff}
```

---

## Flag

```CTFlearn{SkiBanff}```
