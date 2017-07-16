A = list(map(int, input().split()))
d = 0
for i in A:
    for j in A:
        if i == j:
            d += 1
    d -= 1
print(int(d / 2))
