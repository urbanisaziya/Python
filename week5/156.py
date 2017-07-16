x, y = [], []
for i in range(8):
    s, t = list(map(int, input().split()))
    x.append(s)
    y.append(t)
correct = True
for i in range(8):
    for j in range(i + 1, 8):
        a = x[i] - x[j]
        b = y[i] - y[j]
        if x[i] == x[j] or y[i] == y[j] or abs(a) == abs(b):
            correct = False
if correct:
    print('NO')
else:
    print('YES')
