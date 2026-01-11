# Chalkboard

---

## Challenge

Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.

---

## Analisis

Diberikan sebuah file gambar `Math.jpg`:  
  
![Math.jpg](Math.jpg)  
  
Mencoba menggunakan strings untuk melihat plaintext tersembunyi ditemukan informasi:

```text
The flag for this challenge is of the form:
CTFlearn{I_Like_Math_x_y}
where x and y are the solution to these equations:
3x + 5y = 31
7x + 9y = 59
```

---

## Menghitung Flag

### Diketahui:

\[
\begin{cases}
3x + 5y = 31 \quad (1) \\
7x + 9y = 59 \quad (2)
\end{cases}
\]

### 1. Menyamakan koefisien variabel \(y\)

Persamaan (1) dikali 9:
\[
27x + 45y = 279
\]

Persamaan (2) dikali 5:
\[
35x + 45y = 295
\]

### 2. Mengeliminasi variabel \(y\)

\[
(35x + 45y) - (27x + 45y) = 295 - 279
\]

\[
8x = 16
\]

\[
x = 2
\]

### 3. Substitusi nilai \(x\)

Substitusikan \(x = 2\) ke persamaan (1):
\[
3(2) + 5y = 31
\]

\[
6 + 5y = 31
\]

\[
5y = 25
\]

\[
y = 5
\]

### Jawaban Akhir
\[
\boxed{x = 2 \quad \text{dan} \quad y = 5}
\]

---

## Flag 

```CTFlearn{I_Like_Math_2_5}```
