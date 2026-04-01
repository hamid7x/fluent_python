"""Informal Protocol"""


class File:
    def read(self):
        return "reading data"


class DataBase:
    def read(self):
        return "reading Tables"


class Person:
    def read(self):
        return "book"


class Dog():
    pass


def reading_data(obj):
    print(obj.read())


reading_data(File())
reading_data(DataBase())
reading_data(Person())
"""
the problem here is there's
No way to detect errors before runtime
"""
reading_data(Dog())  # crash because read has no read method
