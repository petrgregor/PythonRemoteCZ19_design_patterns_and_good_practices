# Open/close principle

from abc import ABC, abstractmethod


class Operations(ABC):
    @abstractmethod
    def operation(self, list_):
        pass


class Mean(Operations):
    def __init__(self):
        pass

    def operation(self, list_):
        return sum(list_) / len(list_)


class Min(Operations):
    def __init__(self):
        pass

    def operation(self, list_):
        return min(list_)


class Max(Operations):
    def __int__(self):
        pass

    def operation(self, list_):
        return max(list_)


class Main:
    def get_operations(self, list_):
        print(f"Mean is {Mean.operation(list_)}")
        for concrete_operation in Operations.__subclasses__():
            print(concrete_operation.operation(list_))


if __name__ == "__main__":
    m = Main()
    m.get_operations(list_=[1, 2, 3, 4, 5, 6, 7])


