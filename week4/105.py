def power(a, n):
    if n == 0:
        return 1
    return a ** n
a = float(input())
n = int(input())
print(power(a, n))
