import itertools

print(1, *itertools.accumulate(map(int, range(1, int(input())+1)), lambda a, b: a * b))
