nMax1 = int(input())
nMax2 = int(input())
d = 0
if nMax1 < nMax2:
    nMax1, nMax2 = nMax2, nMax1
n = int(input())
while n != 0:
    if n > nMax1:
        nMax2, nMax1 = nMax1, n
    elif n > nMax2:
        nMax2 = n
    n = int(input())
print(nMax2)
