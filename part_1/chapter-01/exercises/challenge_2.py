"""MyRange"""


class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        print(self.start, self.stop)

    def __repr__(self):
        return f"MyRange({self.start}, {self.stop})"

    def __iter__(self):
        current = self.start
        if self.step > 0:
            while current < self.stop:
                yield current
                current += self.step
        else:
            while current > self.stop:
                yield current
                current += self.step

    def __contains__(self, item):
        if self.step > 0:
            return self.start <= item < self.stop and (item - self.start) % self.step == 0
        else:
            return self.stop < item <= self.start and (self.start - item) % (-self.step) == 0


r = MyRange(10, 0, -5)
print(r)
print(r.__iter__())

for x in r:
    print(x, end=' ')
print()
print(5 in r)
r2 = MyRange(0, 20, 5)
print(r2)

for x in r2:
    print(x, end=' ')

print()
for x in range(11, 0, -2):
    print(x, end=' ')
print()

test = None
t = 0
print(test is None)
print(t is None)

print(5 in r2)