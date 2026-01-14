# Basic Android RE 1

## Challenge Overview

A simple APK, reverse engineer the logic, recreate the flag, and submit!  
[BasicAndroidRE1.apk](https://ctflearn.com/challenge/download/962)

---

## Analisis

Challenge ini merupakan **Android Reverse Engineering dasar**. Tujuannya adalah menganalisis logika validasi input di dalam aplikasi Android untuk merekonstruksi flag yang dihasilkan.

APK dibuka menggunakan **jadx-gui** untuk melakukan dekompilasi source code Java.
Pada struktur package ditemukan path berikut:

```
com.example.secondapp
└── MainActivity.java
```

---

## Analisis Source Code

Isi file `MainActivity.java` adalah sebagai berikut:

```java
package com.example.secondapp;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import org.apache.commons.codec.digest.DigestUtils;

/* loaded from: classes.dex */
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
    }

    public void submitPassword(View view) {
        EditText editText = (EditText) findViewById(R.id.editText2);
        if (DigestUtils.md5Hex(editText.getText().toString())
                .equalsIgnoreCase("b74dec4f39d35b6a2e6c48e637c8aedb")) {

            ((TextView) findViewById(R.id.textView))
                .setText("Success! CTFlearn{" 
                + editText.getText().toString() 
                + "_is_not_secure!}");
        }
    }
}
```

---

## Pemahaman Logika Aplikasi

Dari kode di atas dapat disimpulkan:

1. Input pengguna diambil dari `EditText`
2. Input tersebut di-hash menggunakan **MD5**
3. Hash hasil input dibandingkan dengan nilai hardcoded:

```
b74dec4f39d35b6a2e6c48e637c8aedb
```

4. Jika cocok, aplikasi akan menampilkan flag dengan format:

```
CTFlearn{<password>_is_not_secure!}
```

Artinya, kita hanya perlu menemukan **plaintext MD5 hash** tersebut.

---

## Crack MD5 Hash

Hash MD5 di-bruteforce menggunakan **hashcat** dengan wordlist umum.

```bash
hashcat -m 0 hash.txt /usr/share/seclists/Passwords/corporate_passwords.txt
```

### Hasil

```
b74dec4f39d35b6a2e6c48e637c8aedb:Spring2019
```

Password berhasil ditemukan:

```
Spring2019
```

---

## Rekonstruksi Flag

Dengan mengikuti format yang ada di kode aplikasi:

```
CTFlearn{Spring2019_is_not_secure!}
```

---

## Flag

```text
CTFlearn{Spring2019_is_not_secure!}
```
