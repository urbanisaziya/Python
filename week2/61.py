n = int(input())
n1 = 1
n2 = 1
d = 2
if n == 0:
    print(0)
elif n <= 2:
    print(1)
else:
    while d < n:
        b = n1
        n1 = n2
        n2 = n1 + b
        d += 1
    print(n2)
