N = int(input())
A = list(map(int, input().split()))
A.sort()
d = 0
for i in A:
    if i >= N:
        d += 1
        N = i + 3
print(d)
