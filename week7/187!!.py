fin = open('input.txt')
lang = []
New = set()
N = int(fin.readline())
for line in fin:
    line = line.strip()
    if line.isdigit():
        continue
    else:
        lang.append(line)
        if lang.count(line) == N:
            New.add(line)
print(len(New), *(New), sep='\n')
print(len(set(lang)), *(set(lang)), sep='\n')
