A = list(map(int, input().split()))
i = 0
while i < len(A):
    if A[i] == 0:
        A.remove(A[i])
        A.append(0)
        i -= 1
    i += 1
print(*A)
