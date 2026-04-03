"""Object class"""


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


"""
all classes inherite from object class
it's the parent of all classes in python
in this example u can see that
__str__ and __repr__ works even
if we didn't define them
bcause the object class
provide a default
version of them
"""
p = Plant('Rose', 25)
print(p)
print(repr(p))


class PlantOv:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name}, {self.height}"


"""
now in this example we create a class
and override the __str__
and it works that exactly what explain
the output of __mro__ method
u can see the both Plant and PlantOv
inherite from object class
"""
p = PlantOv('Rose', 25)
print(p)
# u can use mro as attribute or call it as method
print(Plant.__mro__)
print(PlantOv.mro())
# (<class '__main__.Plant'>, <class 'object'>)
# (<class '__main__.PlantOv'>, <class 'object'>)

x = 42
print(x.bit_length())
print(x.__class__)
print(x.real)
