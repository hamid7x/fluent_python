
class A:
    x = 1
    z = 5
class B:
    x = 2
    y = 3

class C(A, B):
    pass

obj = C()
print(obj.x)
print(obj.y)
print(obj.z)
print(C.__dict__)
print(C.__mro__)