P = int(input())
X = int(input())
Y = int(input())
summa = X * 100 + Y
vklad_kop = summa * (100 + P)
vklad = vklad_kop // 100
rub = vklad // 100
kop = vklad % 100
print(rub, kop)
