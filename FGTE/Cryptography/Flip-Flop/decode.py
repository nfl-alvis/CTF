def decode(text: str) -> str:
    out = []
    for c in text:
        bits = f"{ord(c):08b}"
        rev = bits[::-1]
        out.append(chr(int(rev, 2)))
    return "".join(out)

if __name__ == "__main__":
    with open("cipher.txt", "rb") as f:
        cipher = f.read().decode("latin-1")

    plain = decode(cipher)
    print(plain)
