n = int(input())
s = 0
d = 1
for i in range(1, n + 1):
    d = d * i
    s += d
print(s)
