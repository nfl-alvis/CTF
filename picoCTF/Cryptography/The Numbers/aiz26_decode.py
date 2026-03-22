def decode_a1z26(cipher_text):
    result = []
    
    for token in cipher_text.split():
        if token.isdigit():
            # Convert number to corresponding letter
            num = int(token)
            if 1 <= num <= 26:
                result.append(chr(num + 96))  # 97 = 'a'
            else:
                result.append('?')
        else:
            # Keep symbols like { }
            result.append(token)
    
    return ''.join(result)


cipher = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
decoded = decode_a1z26(cipher)

print(decoded)
