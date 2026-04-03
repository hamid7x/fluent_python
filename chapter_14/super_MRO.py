"""MRO concepts"""
"""Python follows the order of inheritance"""


class A:
    def hello(self):
        print('A')


class B(A):
    def hello(self):
        print('B')


class C(A):
    def hello(self):
        print('C')


class D(B, C):
    pass


"""
python will looks for hello methods in this order
D first, then B, then C, then A
"""
D().hello()  # prins: B

print(D.__mro__)