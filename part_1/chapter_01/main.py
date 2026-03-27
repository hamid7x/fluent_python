obj = {'name': 'Jhon', 'age': 30}
print(obj.__getitem__('name'))  # dunder method
print(obj['name'])  # built-in method

my_list = [1, 2, 3, 4, 5]
print(my_list.__len__())  # dunder method
print(len(my_list))  # built-in method

x = 10
y = 20
print(x.__add__(y))  # dunder method
print(x + y)  # built-in method
