import itertools

name = ['Joy', "Jim", "Jin"]

# Cycle iterator

cycle = itertools.cycle(name)
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))