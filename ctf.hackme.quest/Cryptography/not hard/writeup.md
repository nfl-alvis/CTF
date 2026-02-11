# not hard

## Deskripsi Challenge

`Nm@rmLsBy{Nm5u-K{iZKPgPMzS2I*lPc%_SMOjQ#O;uV{MM*?PPFhk|Hd;hVPFhq{HaAH<`  
Tips: `pydoc3 base64`

---

## Analisis

Diberikan sebuah ciphertext yang terlihat seperti hasil encoding Base85. Saat mencoba melakukan decode, hasilnya error karena format yang digunakan bukan Base85 standar, melainkan RFC Base85 (Base85 versi Python b85decode) yang memiliki karakter set berbeda dari Ascii85/Base85 biasa.

Berdasarkan hint `pydoc3 base64`, diketahui bahwa Python menyediakan decoder untuk **RFC Base85** melalui fungsi `base64.b85decode()`.

Untuk melakukan decode Base85, digunakan script berikut:

```python
import base64

s = "Nm@rmLsBy{Nm5u-K{iZKPgPMzS2I*lPc%_SMOjQ#O;uV{MM*?PPFhk|Hd;hVPFhq{HaAH<"
print(base64.b85decode(s).decode().strip())
````

Output:

```txt
IZGECR33IRXSA6LPOUQGW3TPO4QGEYLTMUZTEIDFNZRW6ZDJNZTT67I=
```

Hasil tersebut terlihat seperti ciphertext hasil encoding **Base32**. Maka dilakukan decode Base32 pada output tersebut.

```python
import base64

s = "Nm@rmLsBy{Nm5u-K{iZKPgPMzS2I*lPc%_SMOjQ#O;uV{MM*?PPFhk|Hd;hVPFhq{HaAH<"
decoded_b85 = base64.b85decode(s).decode().strip()
print(base64.b32decode(decoded_b85).decode().strip())
```

Output:

```txt
FLAG{Do you know base32 encoding?}
```

---

## Flag

```txt
FLAG{Do you know base32 encoding?}
```
