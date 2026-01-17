# Digital Camouflage

## Challenge Overview

We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: [data.pcap](https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY)  
Hint 1: It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?  
Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.  
  
Credit: picoCTF 2017

---

## Analisis & Eksploitasi

### 1. Membuka File Capture

File `data.pcap` dibuka menggunakan **Wireshark** untuk melakukan analisis traffic jaringan.
Karena proses login web umumnya menggunakan protokol HTTP, dilakukan pemfilteran pada traffic HTTP.

Selain itu, fitur **Follow → HTTP Stream** digunakan untuk melihat percakapan lengkap antara client dan server.

---

### 2. Menemukan Data Login

Pada **HTTP Stream ke-3**, ditemukan sebuah request `POST` yang mengarah ke halaman login:  
  
[login.png](login.png)  
  
```http
POST /pages/main.html HTTP/1.1
```

Di dalam body request tersebut, terdapat parameter login berupa `userid` dan `password`:

```
userid=hardawayn&pswrd=UEFwZHNqUlRhZQ%3D%3D
```

Ini menunjukkan bahwa:

* **Username:** `hardawayn`
* **Password:** masih dalam bentuk encoded

---

### 3. URL Decode

Nilai password mengandung karakter `%3D`, yang menandakan **URL encoding**.
Dilakukan URL decoding terlebih dahulu:

```
UEFwZHNqUlRhZQ%3D%3D
```

Menjadi:

```
UEFwZHNqUlRhZQ==
```

---

### 4. Base64 Decode

String hasil URL decode terlihat jelas merupakan **Base64 encoding**.
Dilakukan decoding Base64 untuk mendapatkan plaintext asli.

Hasil decoding:

```
PApdsjRTae
```

---

## Flag

```text
PApdsjRTae
```
