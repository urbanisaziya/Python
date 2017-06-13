N = int(input())
d1 = N % 10
d2 = N % 100 // 10
d3 = N // 100
answer = d1 + d2 + d3
print(answer)
