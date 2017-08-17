fin = open('input.txt', 'r', encoding='utf8')
school = [0] * 100
for line in fin:
    a = line.split()
    b = int(a[-2])
    school[b] += 1
maxNumber = max(school)
for i in range(len(school)):
    if school[i] == maxNumber:
        print(i, end=' ')
