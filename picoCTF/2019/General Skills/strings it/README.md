# picoCTF 2019 – General Skills: strings it

## Description

Can you find the flag in the file without running it?

<details>
  <summary><h2>Hint</h2></summary>
  strings
</details>

---

## Objective

The objective of this challenge is to extract the flag from a binary file **without executing it**, using static analysis techniques.

---

## Analysis

The provided file is identified as an ELF executable:

```bash
file strings
```

Output:

```
ELF 64-bit LSB pie executable, x86-64, dynamically linked, not stripped
```

Since running unknown binaries can be unsafe, the challenge explicitly requires analyzing it without execution.

A common technique in such cases is to inspect embedded human-readable strings inside the binary.

---

## Approach

We use the `strings` utility to extract printable sequences from the binary:

```bash
strings strings
```

Because the output is large, we filter it using `grep` to locate the flag pattern:

```bash
strings strings | grep -o "picoCTF{[^}]*}"
```

### Explanation

* `strings` extracts readable text from the binary
* `grep -o` ensures only the matching portion is printed
* `picoCTF{[^}]*}` safely captures the flag format without overmatching
