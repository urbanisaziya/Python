A = list(map(int, input().split()))
a = max(A)
for i in A:
    if (i % 2 != 0) and i < a:
        a = i
print(a)
