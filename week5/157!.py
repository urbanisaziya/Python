A = list(map(int, input().split()))
d = 0
for i in range(len(A)):
    j = i - d
    if A[j] == 0:
        A.pop(j)
        A.append(0)
        d += 1
print(*A)
