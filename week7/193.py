N = int(input())
Dict1 = dict()
Dict2 = dict()
for i in range(N):
    line = list(map(str, input().split()))
    Word = line[1]
    Key = line[0]
    Dict1[Key] = Word
    Dict2[Word] = Key
M = input()
if M in Dict1:
    print(Dict1[M])
elif M in Dict2:
    print(Dict2[M])
