def factorec(n):
    return factorec(n-1)*n if n > 1 else 1

print(factorec(6))

### Warning to not do!
#def badrec(x):
#    return badrec(x/2) if x > 0 else 1 # does not finish: x is always superior to 0
#print(badrec(3))
### End warning

def fastexp(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return fastexp(a, b//2)**2
    else:
        return a * fastexp(a, b//2)**2

def fibonacci(n):
    (a, b) = (1, 1) if n == 1 else fibonacci(n - 1)
    return (b, a+b)
print(fibonacci(100)[0])

### Warning to not do!
#def bad_fibonacci(n):
#    x = 1 if n <= 1 else bad_fibonacci(n - 1) + fibonacci(n - 2)
#    return x
#print(bad_fibonacci(100))
### End warning