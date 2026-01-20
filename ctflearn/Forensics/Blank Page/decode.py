#!/usr/bin/python3

data = open("TheMessage.txt", "r").read()

bits = ""
for char in data:
    if ord(char) == 32:
        bits += "0"
    else:
        bits += "1"

decoded = ""
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) == 8:
        decoded += chr(int(byte, 2))

print("=== BITSTREAM ===")
print(bits)
print("\n=== DECODED TEXT ===")
print(decoded)
