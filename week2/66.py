n = int(input())
d = 1
b = 0
while n != 0:
    v = int(input())
    n, v = v, n
    if v == n:
        d += 1
    if d > b:
        b = d
    if n != v:
        d = 1
print(b)
