
# Chalkboard

---

## Challenge

Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.  
[Math.jpg](https://ctflearn.com/challenge/download/972)

---

## Analisis

Diberikan sebuah file gambar bernama `Math.jpg`.  
  
![Math.jpg](Math.jpg)  
  
Untuk mencari petunjuk tersembunyi, dilakukan pemeriksaan string plaintext di dalam file gambar. Dari hasil tersebut diperoleh informasi berikut:

```
The flag for this challenge is of the form:
CTFlearn{I_Like_Math_x_y}

where x and y are the solution to these equations:
3x + 5y = 31
7x + 9y = 59
```

Artinya, nilai `x` dan `y` merupakan solusi dari sistem persamaan linear dua variabel.

---

## Penyelesaian Persamaan

### Persamaan yang Diketahui

```
(1) 3x + 5y = 31
(2) 7x + 9y = 59
```

---

### Langkah 1 – Menyamakan Koefisien y

Kalikan persamaan (1) dengan 9:

```
27x + 45y = 279
```

Kalikan persamaan (2) dengan 5:

```
35x + 45y = 295
```

---

### Langkah 2 – Eliminasi Variabel y

Kurangkan kedua persamaan:

```
(35x + 45y) - (27x + 45y) = 295 - 279
```

Hasil:

```
8x = 16
```

Sehingga:

```
x = 2
```

---

### Langkah 3 – Substitusi Nilai x

Substitusikan `x = 2` ke persamaan (1):

```
3(2) + 5y = 31
6 + 5y = 31
5y = 25
y = 5
```

---

## Hasil Akhir

```
x = 2
y = 5
```

---

## Flag

```text
CTFlearn{I_Like_Math_2_5}
```

