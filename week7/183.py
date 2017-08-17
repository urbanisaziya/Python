N, M = list(map(int, input().split()))
Anya, Borya = [], []
for i in range(N):
    n = int(input())
    Anya.append(n)
for j in range(M):
    m = int(input())
    Borya.append(m)
a = set(Anya)
b = set(Borya)
print(len(a & b))
print(*sorted(list(a & b)))
print(len(a - b))
print(*sorted(list(a - b)))
print(len(b - a))
print(*sorted(list(b - a)))
