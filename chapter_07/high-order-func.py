""""
map → transforms each item, returns new values
filter → tests each item, keeps only the ones that pass
reduce → combines all items into a single value
"""

from functools import reduce


def factorial(n):
    """"return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# map return lazy object
print(map(factorial, [1, 2, 3, 4, 5]))
print(list(map(factorial, [1, 2, 3, 4, 5])))

# with list comprehension
facts = [factorial(n) for n in [1, 2, 3, 4, 5]]
print(facts)


def test_cond(n):
    return n > 10


print(list(filter(test_cond, [1, 11, 3, 30, 1000, 8])))


def add(a, b):
    return a + b


result = reduce(add, [1, 2, 3, 4, 5])
print(result)
