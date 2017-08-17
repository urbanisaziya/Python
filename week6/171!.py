fin = open('input.txt', 'r', encoding='utf8')
max9, max10, max11 = 0, 0, 0
count9, count10, count11 = 0, 0, 0
count9max, count10max, count11max = 0, 0, 0
for line in fin:
    a = line.split()
    b = int(a[-1])
    if a[-2] == '9':
        if b > max9 and max9 == 0:
            max9 = b
            count9 += 1
        elif b >= max9:
            max9 = b
            count9max += 1
    elif a[-2] == '10':
        if b > max10 and max10 == 0:
            max9 = b
            count10 += 1
        elif b >= max10:
            max10 = b
            count10max += 1
    elif a[-2] == '11':
        if b > max11 and max11 == 0:
            max11 = b
            count11 += 1
        elif b >= max11:
            max11 = b
            count11max += 1
count = [count9, count10, count11]
countmax = [count9max, count10max, count11max]
for i in range(len(count)):
    if count[i] <= countmax[i]:
        print(countmax[i], end=' ')
    else:
        print(count[i], end=' ')
