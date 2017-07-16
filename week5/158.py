A = list(map(int, input().split()))
k = A.count(A[0])
c = A[0]
for i in range(len(A)):
    b = A.count(A[i])
    if b > k:
        c = A[i]
        k = b
print(c)
