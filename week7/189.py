N, K = list(map(int, input().split()))
alls = set()
for i in range(K):
    a, b = list(map(int, input().split()))
    days = list(range(a, N + 1, b))
    alls.update(days)
weekend = (set(range(6, N + 1, 7)) | set(range(7, N + 1, 7)))
answer = (alls - weekend)
print(len(answer))
