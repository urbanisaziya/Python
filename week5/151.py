A = list(map(int, input().split()))
a = max(A)
b = min(A)
A.remove(a)
A.remove(b)
c = max(A)
d = min(A)
p1 = a * c
p2 = b * d
if p1 > p2:
    if a > c:
        print(c, a)
    else:
        print(a, c)
else:
    if b > d:
        print(d, b)
    else:
        print(b, d)
