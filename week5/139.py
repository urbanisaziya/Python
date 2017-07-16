A = list(map(int, input().split()))
a = 1000
for i in A:
    if 0 < i < a:
        a = i
print(a)
