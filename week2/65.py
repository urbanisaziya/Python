K = int(input())
N = 1
M = N
n = N
d = 1
while N <= K:
    n = N % 10
    M = N //10
    N +=1
    if n == M:
      d +=1
    print(d)
