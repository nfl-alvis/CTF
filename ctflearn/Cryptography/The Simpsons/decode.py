def octal_to_string(o):
    return ''.join(chr(int(x, 8)) for x in o.split())

def DecodeDat(key, text):
    res = ""
    for i in range(len(text)):
        c = ord(text[i]) - ord('a')
        k = ord(key[i % len(key)]) - ord('a')
        res += chr((c - k) % 26 + ord('a'))
    return res

encoded_octal = "152 162 152 145 162 167 150 172 153 162 145 170 141 162"

question_octal = (
"110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 "
"151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 "
"164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 "
"040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 "
"156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 "
"160 154 165 163 040 146 157 165 162 051"
)

print(octal_to_string(question_octal))

price = 847.63
k = chr(round(price / 8) + 4)
key = k + k + chr(ord(k) - 4)

encoded = octal_to_string(encoded_octal)
print("Flag:", DecodeDat(key, encoded))

