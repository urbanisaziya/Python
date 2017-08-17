N = int(input())
atlas = dict()
for i in range(N):
    line = list(map(str, input().split()))
    country = line[0]
    cities = line[1:]
    for i in range(len(cities)):
        atlas[cities[i]] = country
quest = []
M = int(input())
for j in range(M):
    key = input()
    quest.append(key)
for k in quest:
    print(atlas[k])
