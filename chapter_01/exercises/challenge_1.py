"""Mini List"""


class MiniList:
    def __init__(self, data):
        self._data = data
        self.x = 1000

    def __repr__(self):
        return f"MiniList({self._data})"

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def __getattribute__(self, name):
        print(f'accessing {name}')
        return super().__getattribute__(name)

    def __getattr__(self, name):
        return f"{name} not exist"


obj = MiniList([10, 20, 30, 40])
lst = [1, 2, 3]
print(obj)
print(obj.__dict__)  # get all instance atributes of the object
print(len(obj))
print(obj[0])
print(obj[-1])

for x in obj:
    print(x, end=' ')
print()
print(20 in obj)
print(99 in obj)
print(obj.y)


name = 'hamid'
my_list = [1, 2, 4]
nb = 5
print(len(name))
print(len(my_list))
print(my_list.__getitem__(0))

print(my_list[0])
