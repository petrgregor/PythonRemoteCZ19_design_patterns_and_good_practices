# Interface segregation principle

# BAD solution
"""
from abc import ABC, abstractmethod


class Mammals(ABC):
    @abstractmethod
    def swim(self):
        print("Can swim")

    @abstractmethod
    def walk(self):
        print("Can walk")


class Human(Mammals):
    def swim(self):
        print("Human can swim")

    def walk(self):
        print("Human can walk")


class Whale(Mammals):
    def swim(self):
        print("Whale can swim")

    def walk(self):
        print("Whale can not walk")
        #raise NotImplementedError()


Human().walk()
Human().swim()
Whale().swim()
Whale().walk()
"""

# GOOD solution - Interface segregation principle
from abc import ABC, abstractmethod


class Walker(ABC):
    @abstractmethod
    def walk(self):
        print("can walk")


class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        print("can swim")


class Human(Walker, Swimmer):
    def walk(self):
        print("Human can walk")

    def swim(self):
        print("Human can swim")


class Whale(Swimmer):
    def swim(self):
        print("Whale can swim")


if __name__ == "__main__":
    Human().walk()
    Human().swim()
    Whale().swim()
