s = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

mapping = {
    '!': '1', '@': '2', '#': '3', '$': '4', '%': '5',
    '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'
}

numeric = "".join(mapping.get(c, c) for c in s)
ascii_codes = numeric.split(',')
decoded = ''.join(chr(int(code)) for code in ascii_codes)
print(decoded)
