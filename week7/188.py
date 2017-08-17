A, B, C, D = list(map(int, input().split()))
if A > B:
    bus1 = set(range(B, A + 1))
else:
    bus1 = set(range(A, B + 1))
if C > D:
    bus2 = set(range(D, C + 1))
else:
    bus2 = set(range(C, D + 1))
print(len(bus1 & bus2))
