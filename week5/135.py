def isAscending(B):
    i = 1
    total = len(B)
    s = True
    while i < total:
        s = s and B[i - 1] < B[i]
        i += 1
    return s and 'YES' or 'NO'
A = list(map(int, input().split()))
print(isAscending(A))
