from typing import Protocol


class RestaurentProtocol(Protocol):
    def cook(self) -> str: ...
    def plate(self) -> str: ...
    def clean(self) -> str: ...


class SelfTaughtChef:
    def cook(self) -> str:
        return "i can cook"

    def plate(self) -> str:
        return "i can make plate"

    # def clean(self) -> str:
    #     return "i can clean"


def hire_chef(chef):
    print(chef.cook())
    print(chef.plate())
    print(chef.clean())


chef = SelfTaughtChef()
print(chef.cook())
print(chef.plate())
print(chef.clean())


hire_chef(SelfTaughtChef())
