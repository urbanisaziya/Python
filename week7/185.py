file = open('input.txt', 'r', encoding='utf8')
n = int(file.readline())
answer = set(range(1, n + 1))
for line in file:
    if "YES" in line:
        answer &= temp
    elif "NO" in line:
        answer -= temp
    elif "HELP" not in line:
        temp = set(map(int, line.split()))
print(*sorted(list(answer)))
