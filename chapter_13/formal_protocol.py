"""Formal Protocol"""
from typing import Protocol


class Reader(Protocol):
    def read(self) -> str: ...


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


def reading_data(obj: Reader):
    print(obj.read())


reading_data(File())
reading_data(DataBase())
reading_data(Person())
"""
Now this will get errro when i run mypy .
This help us to debug before run
"""
reading_data(Dog())  # this will crash at run time
