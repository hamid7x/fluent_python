def factorial(n):
    """"return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(2))
print(type(factorial))
print(factorial.__doc__)
fact = factorial
print(fact(5))

"""
both pointing on the object in memory
so both return the same name of the object factorial
"""
print(factorial.__name__)
print(fact.__name__)


def great(name, greeting="Hello"):
    """this function greets someone"""
    return f"{greeting}, {name}"


"""name of the object funtion"""
print(great.__name__)
"""it's docstring"""
print(great.__doc__)
""""it's parameters names"""
print(great.__code__.co_varnames)
""""where it was defined"""
print(great.__code__.co_filename)
"""makes it callable"""
print(great.__call__)
