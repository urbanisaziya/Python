A = int(input())
B = int(input())
n = A
while n != B:
    if n % 2 == 0 and (n / 2) >= B:
        n = n / 2
        print(":2")
    else:
        n = n - 1
        print("-1")
