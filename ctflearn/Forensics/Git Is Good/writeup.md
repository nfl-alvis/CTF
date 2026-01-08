# Git Is Good

---

## Dekripsi

The flag used to be there. But then I redacted it. Good Luck. [Link](https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc)

---

## Analisis

Diberikan file **ZIP Archive** `gitIsGood.zip`.
Setelah mengekstrak arsip ZIP, diperoleh struktur direktori sebagai berikut:

```
gitIsGood/
├── .git/
└── flag.txt
```

Keberadaan direktori `.git` menandakan bahwa folder tersebut merupakan sebuah repository Git lengkap, sehingga seluruh riwayat _commit_ masih tersimpan dan dapat dianalisis.
Ketika membaca isi `flag.txt` hasilnya hanya flag decoy:

```bash
cat flag.txt
```

Output:

```
flag{REDACTED}
```

---

## Analisis Riwayat Commit

Langkah berikutnya adalah melihat riwayat _commit_ menggunakan perintah:

```bash
git log
```


Hasil `git log` menunjukkan beberapa commit sebelumnya:

```
commit d10f77c4e766705ab36c7f31dc47b0c5056666bb (HEAD -> master)
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

commit 195dd65b9f5130d5f8a435c5995159d4d760741b
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:44 2016 -0400

    Edited files

commit 6e824db5ef3b0fa2eb2350f63a9f0fdd9cc7b0bf
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:11 2016 -0400

    edited files

```

Dari riwayat tersebut dapat diasumsikan bahwa flag dihapus atau diubah pada salah satu _commit_ terakhir.

---

## Analisis Perubahan File

Untuk melihat perubahan yang dilakukan pada commit terbaru, digunakan perintah `git show`:

```bash
git show d10f77c4e766705ab36c7f31dc47b0c5056666bb
```

Output menunjukkan perubahan pada berkas `flag.txt`:

```diff
commit d10f77c4e766705ab36c7f31dc47b0c5056666bb (HEAD -> master)
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

diff --git a/flag.txt b/flag.txt
index 8684e68..c5250d0 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +1 @@
-flag{protect_your_git}
+flag{REDACTED}
```

Dari _diff_ tersebut terlihat jelas bahwa flag asli digantikan dengan teks `REDACTED`.

---

## Flag

```flag{REDACTED}```
