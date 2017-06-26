K = int(input())
N = 1
m = N
n = N
count = 0
while N <= K:
    n = N // 10
    m = N % 10
    if n == m or n ==0:
        count += 1
    N += 1
print(count)

#not work