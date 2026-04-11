""""lambda"""


# normal way
def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]
print(list(map(double, numbers)))


# since we only have simple
# function we can just use
# anynomys function called lambda
print(list(map(lambda x: x * 2, numbers)))
