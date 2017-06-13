v = int(input())
t = int(input())
if v > 0:
    d1 = (v * t) % 109
    print(d1)
else:
    d2 = -1 * (((-1 * v * t) % (-1 * 109)))
    print(d2)
