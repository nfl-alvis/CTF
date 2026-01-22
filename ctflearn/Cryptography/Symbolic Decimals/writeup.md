# Symbolic Decimals

## Deskripsi Challenge

Did you know that you can hide messages with symbols? For example, `!@#$%^&*(` is `123456789!`  
Now Try: `^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%`  
However, this isn't as easy as you might think.

---

## Analisis

Dari contoh yang diberikan, dapat disimpulkan adanya **mapping simbol ke digit desimal** sebagai berikut:

```
 ! = 1
 @ = 2
 # = 3
 $ = 4
 % = 5
 ^ = 6
 & = 7
 * = 8
 ( = 9
 ) = 0
```

Ciphertext dipisahkan oleh tanda koma (`,`), yang mengindikasikan bahwa setiap grup simbol merepresentasikan **kode ASCII dalam bentuk desimal**.

Dengan demikian, proses decoding dilakukan dalam dua tahap:

1. Mengonversi simbol menjadi digit berdasarkan mapping.
2. Mengonversi hasil digit desimal menjadi karakter ASCII.

---

## Proses Decode

Untuk mempercepat dan meminimalkan kesalahan, proses decoding dilakukan menggunakan script Python sederhana berikut:

```python
s = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

mapping = {
    '!': '1', '@': '2', '#': '3', '$': '4', '%': '5',
    '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'
}

numeric = "".join(mapping.get(c, c) for c in s)

ascii_codes = numeric.split(',')
decoded = ''.join(chr(int(code)) for code in ascii_codes)

print(decoded)
```

### Penjelasan Script

* Setiap simbol dikonversi menjadi digit sesuai mapping.
* Hasilnya berupa deretan angka desimal yang dipisahkan koma.
* Setiap angka kemudian diubah menjadi karakter menggunakan konversi ASCII.

---

## Hasil

Setelah menjalankan script di atas, diperoleh output:

```
CTF{Star_._Wars_._For_._Life}
```

---

## Flag

```text
CTF{Star_._Wars_._For_._Life}
```
