from random import shuffle, randrange

def cipher(s):
    key = [ chr(i + 65) for i in range (26) ]
    shuffle(key)
    out = ""
    for c in s:
        ascii = ord(c)
        if ascii > 64 and ascii < 91:
            out += key[ascii - 65]
        else:
            out += c
    return out

def cipher2(s, k):
    key = [ randrange(1, 27) for i in range(k) ]
    out = ""
    i = 0
    for c in s:
        out += chr((ord(c) - 65 + key[i]) % 26 + 65)
        i = (i + 1) % k
    return out

print(cipher( "BONNE NUIT LES PETITS "))
print(cipher2("OHMONBATEAUQUILESTBEAU", 4))