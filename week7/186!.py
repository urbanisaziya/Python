file = open('input.txt', 'r', encoding='utf8')
n = int(file.readline())
answer = set(range(1, n + 1))
for line in file:
    if "HELP" not in line:
        temp = set(map(int, line.split()))
        no = answer - temp
        yes = answer & temp
        if len(no) < len(yes):
            answer = yes
            print('YES')
        else:
            answer = no
            print('NO')
    else:
        break
print(*sorted(list(answer)))
