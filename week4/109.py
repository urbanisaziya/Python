def ReduceFraction(a, b):
    if a % b == 0:
        return n // b, m // b
    return ReduceFraction(b, a % b)
n = int(input())
m = int(input())
p, q = ReduceFraction(n, m)
print(p, q)
