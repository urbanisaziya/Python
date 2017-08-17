fin = open('input.txt', 'r', encoding='utf8')
sum9 = 0
count9 = 0
sum10 = 0
count10 = 0
sum11 = 0
count11 = 0
for line in fin:
    a = line.split()
    b = int(a[-1])
    if a[-2] == '9':
        sum9 += b
        count9 += 1
    elif a[-2] == '10':
        sum10 += b
        count10 += 1
    elif a[-2] == '11':
        sum11 += b
        count11 += 1
print(sum9/count9, end=' ')
print(sum10/count10, end=' ')
print(sum11/count11, end='')
