A = list(map(int, input().split()))
k = int(input())
A.pop(k)
print(*A)
