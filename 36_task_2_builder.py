"""
Write a program that will transform the data read from the text file,
character by character with the help of Builders, into characters:

    hexadecimal values
    capital letters
    lowercase letters
    character counter
"""


class Builder:
    def build_part(self, element):
        pass

    def get_result(self):
        pass


class HexBuilder(Builder):
    def __init__(self):
        self._result = ""

    def build_part(self, element):
        self._result += hex(ord(element))
        self._result += " "

    def get_result(self):
        return self._result


class CapitalLettersBuilder(Builder):
    def __init__(self):
        self._result = ""

    def build_part(self, element):
        self._result += element.upper()

    def get_result(self):
        return self._result


class LowerCaseLettersBuilder(Builder):
    def __init__(self):
        self._result = ""

    def build_part(self, element):
        self._result += element.lower()

    def get_result(self):
        return self._result


class CharacterCounterBuilder(Builder):
    def __init__(self):
        self._result = 0

    def build_part(self, element):
        self._result += 1

    def get_result(self):
        return self._result


class Director:
    def __init__(self, file_name):
        self._file_name = file_name
        self._builder = None

    def construct(self):
        with open(self._file_name, "r") as file:
            for line in file:
                for char in line:
                    self._builder.build_part(char)

    def set_builder(self, builder):
        self._builder = builder

    def get_result(self):
        return self._builder.get_result()


def main():
    director = Director("07_singleton.py")

    """
    my_builder = HexBuilder()
    director.set_builder(my_builder)
    director.construct()
    print(director.get_result())

    my_builder = CapitalLettersBuilder()
    director.set_builder(my_builder)
    director.construct()
    print(director.get_result())

    my_builder = LowerCaseLettersBuilder()
    director.set_builder(my_builder)
    director.construct()
    print(director.get_result())

    my_builder = CharacterCounterBuilder()
    director.set_builder(my_builder)
    director.construct()
    print(f"Number of characters: {director.get_result()}")
    """

    for my_builder in [HexBuilder(),
                       CapitalLettersBuilder(),
                       LowerCaseLettersBuilder(),
                       CharacterCounterBuilder()]:
        director.set_builder(my_builder)
        director.construct()
        print(director.get_result())


if __name__ == "__main__":
    main()
