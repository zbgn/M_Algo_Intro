from random import shuffle, randrange

def kill(t, u):
    out, key = t, [ chr(i + 65) for i in range(26)]
    while u not in out:
        shuffle(key)
        out= ""
        for c in t:
            ascii =  ord(c)
            if ascii > 64 and ascii < 91:
                out += key[ascii - 65]
            else:
                out += c
    return out

def kill2(t, k, u):
    out = t
    while not u in out:
        key = [ randrange(1, 27) for i in range(k) ]
        out, i = "", 0
        for c in t:
            out = chr((ord(c) - 65 + key[i]) % 26 + 65)
            i = (i + 1) % k
    return out

print(kill("QJFFO FMGX ZOH BOXGXH", "PETITS"))
print(kill2("LBJNKVXSBURPRCIDPNYDXO", 4, "ESTBEAU"))
