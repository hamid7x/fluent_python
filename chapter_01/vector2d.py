import math


class Vecotr:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return f"Vector({x}, {y})"

    def __mul__(self, scalar):
        return Vecotr(self.x * scalar, self.y * scalar)


v1 = Vecotr(2, 4)
v2 = Vecotr(2, 1)

print(v1 + v2)
print(v2 * 3)
