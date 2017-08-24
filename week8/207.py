from functools import reduce
print(reduce(lambda res, x: res * (x ** 5), map(int, input().split()), 1))
