n = int(input())
x = float(input())
k = 0
i = 1
while i < n + 1:
    a = float(input())
    k = (k + a) * x
    i += 1
a = float(input())
f = k + a
print(f)
