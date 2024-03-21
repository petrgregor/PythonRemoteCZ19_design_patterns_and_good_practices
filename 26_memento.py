class SimpleClass:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return f"SimpleClass('{self.name}', {self.count})"

    def set_count(self, value):
        self.count = value


sc1 = SimpleClass('test', 10)
print(sc1)
repr = repr(sc1)
sc1.set_count(20)
print(sc1)
sc2 = eval(repr)
print(sc2)
