letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(arg, m=3):
    cipher = letters+letters
    cipher = cipher[m:(m+26)]
    ans = ""
    for c in arg:
        if (c >= "A") and (c <= "Z"):
            c = cipher[letters.find(c)]
        ans += c
    return ans

def decode(arg, m=3):
    cipher = letters+letters
    cipher = cipher[m:(m+26)]
    ans = ""
    for c in arg:
        if (c >= "A") and (c <= "Z"):
            c = letters[cipher.find(c)]
        ans += c
    return ans

msg = "ALL GAUL IS DIVIDED INTO THREE PARTS"
enc = encode(msg)
dec = decode(enc)
print(msg)
print(enc)
print(dec)

