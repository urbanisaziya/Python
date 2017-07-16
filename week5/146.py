A = list(map(int, input().split()))
X = int(input())
i = 0
while i < len(A) and A[i] >= X:
    i += 1
print(i + 1)
