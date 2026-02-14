import re

OOK = {
    (".", "?"): ">", ("?", "."): "<", (".", "."): "+", ("!", "!"): "-",
    ("!", "."): ".", (".", "!"): ",", ("!", "?"): "[", ("?", "!"): "]",
}

TOK = {
    "greater_than": ">", "less_than": "<", "plus": "+", "minus": "-",
    "dot": ".", "comma": ",", "left_bracket": "[", "right_bracket": "]",
    "space": "",
}

TOKS = sorted(TOK, key=len, reverse=True)

def bf_run(code, inp=""):
    tape, ptr, ip, in_i, out = [0]*30000, 0, 0, 0, []
    st, j = [], {}
    for i, c in enumerate(code):
        if c == "[": st.append(i)
        elif c == "]":
            a = st.pop()
            j[i] = a
            j[a] = i
    while ip < len(code):
        c = code[ip]
        if c == ">": ptr += 1
        elif c == "<": ptr -= 1
        elif c == "+": tape[ptr] = (tape[ptr] + 1) & 255
        elif c == "-": tape[ptr] = (tape[ptr] - 1) & 255
        elif c == ".": out.append(chr(tape[ptr]))
        elif c == ",":
            tape[ptr] = ord(inp[in_i]) & 255 if in_i < len(inp) else 0
            in_i += 1
        elif c == "[" and tape[ptr] == 0: ip = j[ip]
        elif c == "]" and tape[ptr] != 0: ip = j[ip]
        ip += 1
    return "".join(out)

def ook_to_bf(s):
    x = re.findall(r"[.?!]", s)
    return "".join(OOK[(x[i], x[i+1])] for i in range(0, len(x), 2))

def tok_to_bf(s):
    s, i, out = s.lower(), 0, []
    while i < len(s):
        for t in TOKS:
            if s.startswith(t, i):
                out.append(TOK[t])
                i += len(t)
                break
        else:
            i += 1
    return "".join(out)

def nums_to_ascii(s):
    nums = list(map(int, re.findall(r"\d+", s)))
    return "".join(map(chr, nums))

if __name__ == "__main__":
    data = open("brain_dead.bf", "r", encoding="utf-8").read()
    stage1 = bf_run(ook_to_bf(data))
    stage2 = bf_run(tok_to_bf(stage1))
    print(nums_to_ascii(stage2))
