import itertools

n = int(input())
numbers = list(range(1, n+1))
print(*itertools.permutations(numbers), sep='\n')

