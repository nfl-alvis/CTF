# Tone Dialing

## Challenge

At 1pm I called my uncle who was 64 years old 10 months ago, but I heard only that. Later I started thinking about the 24 hour clock.  
I hope you will help me solve this problem.  
[you_know_what_to_do.wav](https://ctflearn.com/challenge/download/889)

---

## Analisis

Diberikan sebuah file audio bernama `you_know_what_to_do.wav`. Ketika diputar, audio tersebut tidak berisi suara percakapan manusia, melainkan bunyi nada pendek yang menyerupai suara tombol telepon klasik.  
  
<audio controls>
  <source src="you_know_what_to_do.wav?raw=true" type="audio/wav">
</audio>  
  
Karakteristik suara tersebut identik dengan **DTMF (Dual-Tone Multi-Frequency)**, yaitu sistem nada yang digunakan pada keypad telepon untuk merepresentasikan angka (0–9) dan simbol tertentu.

Berdasarkan deskripsi challenge dan jenis audio yang diberikan, dapat diasumsikan bahwa informasi penting (flag) tersembunyi dalam bentuk **DTMF tone sequence**.

---

## Decoding Process

Untuk mengekstrak digit dari nada DTMF, audio dianalisis menggunakan decoder online:

[**DTMF Decoder**](https://dtmf.netlify.app/)

Setelah file audio diunggah dan diproses, diperoleh hasil decoding berupa deretan angka:

```
67847010810197110123678289808479718265807289125
```

---

## Interpreting the Result

Deretan angka tersebut kemudian diasumsikan sebagai representasi **ASCII decimal codes** yang digabungkan.

Dengan memisahkan angka ke dalam nilai ASCII yang valid dan mengonversinya ke karakter, diperoleh string berikut:

```
CTFlearn{CRYPTOGRAPHY}
```

---

## Flag

```text
CTFlearn{CRYPTOGRAPHY}
```
