class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"


class Line:
    def draw(self, length):
        pass

    def starting_point(self):
        pass

    def starting_point(self, value):
        pass


class SolidLine(Line):
    def __init__(self):
        self._point = Point(0, 0)

    def draw(self, length):
        print(f"Drawing solid line starting in {self._point} with length {length}")

    @property
    def starting_point(self):
        return self._point

    @starting_point.setter
    def starting_point(self, value):
        self._point = value


class DottedLine(Line):
    def __init__(self):
        self._point = Point(0, 0)

    def draw(self, length):
        print(f"Drawing dotted line starting in {self._point} with length {length}")

    @property
    def starting_point(self):
        return self._point

    @starting_point.setter
    def starting_point(self, value):
        self._point = value


class CompoundLine(Line):
    def __init__(self):
        self._lines = []

    def draw(self, length):
        for line in self._lines:
            line.draw(length)

    @property
    def starting_point(self):
        if not self._lines:
            return Point(0, 0)
        else:
            return self._lines[0].starting_point()

    @starting_point.setter
    def starting_point(self, value):
        for line in self._lines:
            line.starting_point = value

    def add_line(self, line):
        self._lines.append(line)

    def remove_line(self, line):
        self._lines.remove(line)


def main():
    dotted1 = DottedLine()
    dotted1.starting_point = (1, 1)

    dotted2 = DottedLine()
    dotted2.starting_point = (2, 2)

    solid1 = SolidLine()
    solid1.starting_point = (3, 3)

    solid2 = SolidLine()
    solid2.starting_point = (4, 4)

    compound1 = CompoundLine()
    compound2 = CompoundLine()

    compound1.add_line(dotted1)
    compound1.add_line(solid1)
    compound1.add_line(compound2)
    compound2.add_line(dotted2)
    compound2.add_line(solid2)

    compound2.starting_point = (5, 5)
    print("Compound 1 v. 1:")
    compound1.draw(5)

    compound1.starting_point = (10, 10)
    print("Compound 1 v. 2:")
    compound1.draw(10)

    solid2.starting_point = (20, 20)
    print("Compound 1 v. 3:")
    compound1.draw(15)

    print("Compound 2 v. 1:")
    compound2.draw(15)

if __name__ == '__main__':
    main()
