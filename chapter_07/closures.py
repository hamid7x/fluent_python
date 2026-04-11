numbers = []


def averge(new_number):
    numbers.append(new_number)
    return sum(numbers) / len(numbers)


print(averge(10))
print(averge(20))
print(averge(30))


def make_averge():
    numbers = []

    def averge(new_number):
        numbers.append(new_number)
        return sum(numbers) / len(numbers)

    return averge


print()
avg = make_averge()
print(avg(10))
print(avg(20))
print(avg(30))
print(avg.__code__.co_freevars)
print(avg.__closure__)


def make_averager():
    count = 0
    total = 0
    
    def average(new_number):
        # nonlocal count, total
        # count += 1
        # total += new_number
        count = 1
        return total / count
    
    return average

avgv = make_averager()
print(avgv(10))