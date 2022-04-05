from random import seed, shuffle
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(arg):
    seed(8675309)
    ans = ""
    for c in arg:
        cipher = [i for i in letters]
        shuffle(cipher)
        cipher = "".join(cipher)
        if (c >= "A") and (c <= "Z"):
            c = cipher[letters.find(c)]
        ans += c
    return ans

def decode(arg):
    seed(8675309)
    ans = ""
    for c in arg:
        cipher = [i for i in letters]
        shuffle(cipher)
        cipher = "".join(cipher)
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

