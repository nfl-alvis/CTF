# r u kddding

## Deskripsi Challenge

EKZF{Hs'r snnn dzrx, itrs bzdrzq bhogdq}

---

## Analisis

Diberikan sebuah ciphertext yang merupakan hasil enkripsi **Caesar Cipher**.

Dari format flag, dapat diasumsikan bahwa prefix seharusnya adalah `FLAG{`. Namun pada ciphertext tertulis `EKZF{`, sehingga dapat disimpulkan bahwa teks telah mengalami pergeseran **-1**.

Untuk melakukan dekripsi, alphabet perlu digeser sebanyak **+1**. Proses ini dapat dilakukan menggunakan `tr` dengan command berikut:

```bash
echo "EKZF{Hs'r snnn dzrx, itrs bzdrzq bhogdq}" | tr 'a-zA-Z' 'b-zaB-ZA'
````

Output:

```txt
FLAG{It's tooo easy, just caesar cipher}
```

---

## Flag

```txt
FLAG{It's tooo easy, just caesar cipher}
```

