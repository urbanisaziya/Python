def MinDivisor(n):
    min = 2
    while min ** 2 <= n and n % min != 0:
        min += 1
    if min > n**(1/2):
        return n
    else:
        return min
n = int(input())
print(MinDivisor(n))
