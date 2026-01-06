# Morse Code

## Deskripsi

..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...

---

## Analisis 

Diberikan sebuah _string_ berpola titik (`.`) dan garis (`-`) yang dipisahkan oleh spasi merupakan karakteristik standar **Kode Morse**.

```
..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...
```

---

## Proses Decode

Proses decoding dilakukan dengan menerjemahkan Kode Morse ke teks ASCII dengan _command_ berikut:

```bash
echo "..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ..." | morse2ascii -
```

Output:

```
- decoded morse data:
flagsamuelmorseiscoolbythewayilikechees
```

---

## Flag 

```flagsamuelmorseiscoolbythewayilikechees```

