# easy

## Deskripsi Challenge

526b78425233745561476c7a49476c7a4947566863336b7349484a705a3268305033303d

---

## Analisis

Diberikan sebuah ciphertext yang terlihat seperti hasil encoding **hex**. Langkah pertama adalah melakukan decode hex menggunakan `xxd`.

```bash
echo "526b78425233745561476c7a49476c7a4947566863336b7349484a705a3268305033303d" | xxd -r -p
````

Output yang dihasilkan:

```txt
RkxBR3tUaGlzIGlzIGVhc3ksIHJpZ2h0P30=
```

Hasil decode tersebut masih terlihat seperti ciphertext hasil encoding **Base64**. Maka langkah berikutnya adalah melakukan decode Base64.

```bash
echo "526b78425233745561476c7a49476c7a4947566863336b7349484a705a3268305033303d" | xxd -r -p | base64 -d
```

Output:

```txt
FLAG{This is easy, right?}
```

---

## Flag

```txt
FLAG{This is easy, right?}
```

