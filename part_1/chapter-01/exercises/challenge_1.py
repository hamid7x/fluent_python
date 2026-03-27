"""Mini List"""


class MiniList:
    def __init__(self, data):
        self._data = data

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


obj = MiniList([10, 20, 30, 40])

print(obj)

print(len(obj))
print(obj[0])
print(obj[-1])

for x in obj:
    print(x, end=' ')
print()
print(20 in obj)
print(99 in obj)
