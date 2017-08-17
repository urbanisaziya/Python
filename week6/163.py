S, N = list(map(int, input().split()))
k = []
for i in range(N):
    n = int(input())
    k.append(n)
k.sort()
d = 0
for x in k:
    if x < S:
        S = S - x
        d += 1
print(d)
