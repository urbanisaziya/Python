n = int(input())
oneList = list(map(int, input().split()))
m = int(input())
twoList = list(map(int, input().split()))
home = []
for x in range(len(oneList)):
    home.append((oneList[x], x))
bomb = []
for y in range(len(twoList)):
    bomb.append((twoList[y], y + 1))
home.sort()
bomb.sort()
result = [0] * n
j = 0
for i in range(len(home)):
    if home[i][0] < bomb[j][0] and j == 0:
        result[home[i][1]] = (bomb[0][1])
    elif j >= len(bomb) - 1:
        result[home[i][1]] = (bomb[-1][1])
    else:
        dist = home[i][0]
        while j < len(bomb) - 1:
            dl = bomb[j][0]
            dr = bomb[j + 1][0]
            if dist >= dl and dist <= dr:
                break
            else:
                j += 1
        if j < len(bomb) - 1:
            if abs(dist - bomb[j][0]) < abs(dist - bomb[j + 1][0]):
                result[home[i][1]] = bomb[j][1]
            else:
                result[home[i][1]] = bomb[j + 1][1]
        else:
            result[home[i][1]] = (bomb[-1][1])
print(*result)
