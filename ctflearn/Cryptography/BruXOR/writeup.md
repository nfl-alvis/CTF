# BruXOR

---

## Deskripsi

There is a technique called bruteforce. 
Message: q{vpln'bH_varHuebcrqxetrHOXEj 
No key! Just brute .. brute .. brute ... :D

---

## Analisis

Diberikan _encrypted string_ hasil `XOR` dengan key yang belum diketahui, di deskripsi _challenge_ disebutkan `"Brute"` yang dapat diartikan kita harus bruteforce kunci tersebut. 

---

## Proses Decrypt

Mendecrypt di [CyberChef](https://gchq.github.io/CyberChef) dengan Resep `XOR Brute Force`.
Pada hasil bruteforce, ditemukan plaintext yang valid pada key = 17, dengan hasil sebagai berikut:
![Decrypted.png](Decrypted.png)

`Key = 17: flag{y0u_Have_bruteforce_XOR}`

---

## Flag

```flag{y0u_Have_bruteforce_XOR}```
