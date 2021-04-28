# Digit Counter

def digitCounter(n):
    if n == 0:
        return 0
    return 1+digitCounter(n//10)

print(digitCounter(1234))




#### integer exponentiation
def exponent(x, y):
    if y == 0:
        return 1
    return x*exponent(x, y-1)

print(exponent(2, 4))

