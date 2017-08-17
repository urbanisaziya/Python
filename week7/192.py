fin = open('input.txt', 'r', encoding='utf8')
List = dict()
for line in fin:
    line = line.strip().split()
    for i in line:
        List[i] = List.get(i, 0) + 1
        print(List[i] - 1, end=' ')
