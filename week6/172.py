fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
grade = []
for line in fin:
    K = int(line)
    break
for line in fin:
    a = line.split()
    if (int(a[-3]) >= 40) and (int(a[-2]) >= 40) and (int(a[-1]) >= 40):
        b = int(a[-3]) + int(a[-2]) + int(a[-1])
        grade.append(b)
grade.sort(reverse=True)
j = 0
if len(grade) == K:
    print(0, file=fout)
elif len(grade) > K:
    if grade[0] == grade[K]:
        print(1, file=fout)
    else:
        while grade[K - 1 - j] == grade[K - j]:
            if grade[K - 1 - j] == grade[K - j]:
                j += 1
        print(grade[K - 1 - j], file=fout)
else:
    print(0, file=fout)
fin.close()
fout.close()
