n = int(input())
nMax = n
d = 0
while n != 0:
    if n > nMax:
        if n - nMax > 0:
            d = d + 1
    nMax = n
    n = int(input())
print(d)
