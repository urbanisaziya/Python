def IsPrime(n):
    min = 2
    while min ** 2 <= n and n % min != 0:
        min += 1
    if min > n ** (1 / 2):
        return True
    else:
        return False
n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
