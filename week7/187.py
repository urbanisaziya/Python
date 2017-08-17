fin = open('input.txt')
lang = set()
study = set()
temp = set()
flag = False
count = 0
total = 0
N = int(fin.readline())
for line in fin:
    line = line.strip()
    if line.isdigit():
        total = int(line)
        count = 0
        if not flag and len(lang) > 0:
            flag = True
        continue
    else:
        count += 1
        study.add(line)
        if flag:
            temp.add(line)
        else:
            lang.add(line)
        if flag and total == count:
            lang = lang & temp
            temp = set()
print(len(lang), *lang, sep='\n')
print(len(study), *study, sep='\n')
