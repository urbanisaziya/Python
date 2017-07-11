def result(k):
    n = int(input())
    if n == 0:
        print(k)
    else:
        result(n+k)
result(0)
