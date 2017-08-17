fin = open('input.txt', 'r', encoding='utf8')
spisok =[]
list = dict()
for line in fin:
    line = line.strip().split()
    Key = line[0]
    Result = int(line[-1])
    list[Key] = Result
    print(list)
a = sum(list.values())
b = a // 450
print(a,b)




