A = list(map(int, input().split()))
count = 0
a = max(A)
for i in range(len(A)):
    if A[i] >= a:
        a = A[i]
        count = i
print(a, count)
