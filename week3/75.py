P = int(input())
X = int(input())
Y = int(input())
K = int(input())
i = 1
summa = X * 100 + Y
while i <= K:
    vklad = summa * (100 + P)
    summa = vklad // 100
    i += 1
rub = summa // 100
kop = summa % 100
print(rub, kop)
