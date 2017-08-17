fin = open('input.txt', 'r', encoding='utf8')
List = dict()
for line in fin:
    line = line.strip().split()
    Key = line[0]
    Result = int(line[1])
    if Key in List:
        List[Key] += Result
    else:
        List[Key] = Result
for Key in sorted(List):
    print(Key, List[Key])
