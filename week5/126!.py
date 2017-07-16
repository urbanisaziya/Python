a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a + b + c + d != 0:
    print(0)
for i in range(1, 1000):
    if a == b == c == d == 0:
        print(i)
    elif a * (i ** 3) + b * (i ** 2) + c * i + d == 0:
        print(i)
