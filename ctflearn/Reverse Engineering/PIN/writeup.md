# PIN

## Challenge

Can you crack my pin?  
[rev1](https://mega.nz/#!PXYjCKCY!F2gcs83XD6RxjOR-FNWGQZpyvUFvDbuT-PTnqRhBPGQ)

---

## Analisis

Challenge ini merupakan **reverse engineering binary ELF** sederhana. Program meminta input berupa **PIN** dan akan memverifikasi apakah nilai yang dimasukkan benar atau tidak.  
Menjalankan binary secara langsung:

```bash
./rev1
```

Output:

```
Masukan PIN =
```

Ini mengindikasikan bahwa program menunggu input numerik dari pengguna.

---

## Analisis Static (Disassembly)

Binary dianalisis menggunakan **GDB + pwndbg**.
Disassembly fungsi `main` menunjukkan alur program sebagai berikut:

```asm
Dump of assembler code for function main:
   0x00000000004005d6 <+0>:     push   rbp
   0x00000000004005d7 <+1>:     mov    rbp,rsp
   0x00000000004005da <+4>:     sub    rsp,0x10
   0x00000000004005de <+8>:     lea    rdi,[rip+0xdf]        # 0x4006c4
   0x00000000004005e5 <+15>:    mov    eax,0x0
   0x00000000004005ea <+20>:    call   0x4004a0 <printf@plt>
   0x00000000004005ef <+25>:    lea    rax,[rbp-0x4]
   0x00000000004005f3 <+29>:    mov    rsi,rax
   0x00000000004005f6 <+32>:    lea    rdi,[rip+0xd6]        # 0x4006d3
   0x00000000004005fd <+39>:    mov    eax,0x0
   0x0000000000400602 <+44>:    call   0x4004b0 <__isoc99_scanf@plt>
   0x0000000000400607 <+49>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040060a <+52>:    mov    edi,eax
   0x000000000040060c <+54>:    call   0x4005b6 <cek>
   0x0000000000400611 <+59>:    test   eax,eax
   0x0000000000400613 <+61>:    je     0x400623 <main+77>
   0x0000000000400615 <+63>:    lea    rdi,[rip+0xba]        # 0x4006d6
   0x000000000040061c <+70>:    call   0x400490 <puts@plt>
   0x0000000000400621 <+75>:    jmp    0x40062f <main+89>
   0x0000000000400623 <+77>:    lea    rdi,[rip+0xba]        # 0x4006e4
   0x000000000040062a <+84>:    call   0x400490 <puts@plt>
   0x000000000040062f <+89>:    mov    eax,0x0
   0x0000000000400634 <+94>:    leave
   0x0000000000400635 <+95>:    ret
```

Dari sini terlihat bahwa:

1. Input PIN dibaca menggunakan `scanf`
2. Nilai PIN dikirim sebagai argumen ke fungsi `cek`
3. Return value dari `cek` menentukan apakah PIN benar atau salah

---

## Analisis Fungsi `cek`

Disassembly fungsi `cek`:

```asm
Dump of assembler code for function cek:
   0x00000000004005b6 <+0>:     push   rbp
   0x00000000004005b7 <+1>:     mov    rbp,rsp
   0x00000000004005ba <+4>:     mov    DWORD PTR [rbp-0x4],edi
   0x00000000004005bd <+7>:     mov    eax,DWORD PTR [rip+0x200a7d]        # 0x601040 <valid>
   0x00000000004005c3 <+13>:    cmp    DWORD PTR [rbp-0x4],eax
   0x00000000004005c6 <+16>:    jne    0x4005cf <cek+25>
   0x00000000004005c8 <+18>:    mov    eax,0x1
   0x00000000004005cd <+23>:    jmp    0x4005d4 <cek+30>
   0x00000000004005cf <+25>:    mov    eax,0x0
   0x00000000004005d4 <+30>:    pop    rbp
   0x00000000004005d5 <+31>:    ret
```

Fungsi `cek` hanya melakukan **perbandingan langsung** antara input PIN dan sebuah **variabel global** bernama `valid`.

---

## Mengambil Nilai PIN Valid

Alamat variabel global `valid` berada di:

```
0x601040
```

Membaca nilainya di GDB:

```bash
x/w 0x601040
```

Output:

```
0x601040 <valid>: 333333
```

Artinya, PIN yang dianggap valid oleh program adalah:

```
333333
```

---

## Flag

```text
333333
```
