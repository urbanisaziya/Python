n = int(input())
nMax = n
d = 1
while n != 0:
    n = int(input())
    if n > nMax:
        nMax = n
        d = 1
    elif n == nMax:
        d = d + 1
print(d)
