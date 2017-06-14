n = int(input())
n1 = 0
n2 = 1
d = 1
if n == 0:
    print(0)
else:
    while n2 <= n:
        if n2 == n:
            print(d)
            break
        n1, n2 = n2, n1 + n2
        d += 1
    else:
        print(-1)
