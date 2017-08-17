N = int(input())
spisok = []
for i in range(N):
    n, b = input().split()
    b = int(b)
    spisok.append((n, b))
spisok.sort(reverse=True, key=lambda x: x[1])
for j in range(len(spisok)):
    print(spisok[j][0])
