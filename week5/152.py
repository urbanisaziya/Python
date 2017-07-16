A = list(map(int, input().split()))
if len(A) == 3:
    print(*A)
elif len(A) == 4:
    a = max(A)
    b = min(A)
    A.remove(a)
    A.remove(b)
    c = max(A)
    d = min(A)
    if b < 0 and d > 0:
        print(a, c, d)
    elif b > 0 and d > 0:
        print(a, c, b)
    else:
        p1 = a * c * b
        p2 = a * c * d
        if p1 > p2:
            print(a, c, b)
        else:
            print(a, c, d)
else:
    a = max(A)
    b = min(A)
    A.remove(a)
    A.remove(b)
    c = max(A)
    d = min(A)
    A.remove(c)
    A.remove(d)
    e = max(A)
    p1 = a * c * e
    p2 = b * d * a
    if p1 > p2:
        print(a, c, e)
    else:
        print(b, d, a)
