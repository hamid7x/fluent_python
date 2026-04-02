from abc import ABC, abstractmethod


class RestaurantSchool(ABC):   # the school — can't instantiate directly
    @abstractmethod
    def cook(self) -> str: ...   # just defining the rule, no implementation
    @abstractmethod
    def plate(self) -> str: ...
    @abstractmethod
    def clean(self) -> str: ...


class Chef(RestaurantSchool):  # Chef MUST graduate from the school
    def cook(self):
        return "i can cook"  # Chef decides HOW

    def plate(self):
        return "i can make plate"

    # def clean(self):
        # return "i can clean"


def hire_chef(chef):
    print(chef.cook())
    print(chef.plate())
    print(chef.clean())


hire_chef(Chef())
