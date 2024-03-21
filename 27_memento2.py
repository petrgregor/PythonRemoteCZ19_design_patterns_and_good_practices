import pickle


class NotSoSimpleClass:
    def __init__(self, name='', count=0):
        self.name = name
        self.count = count

    def get_state(self):
        return pickle.dumps(self.__dict__)

    def restore_state(self, memento):
        self.__dict__.clear()
        self.__dict__.update(pickle.loads(memento))

    def set_count(self, value):
        self.count = value

    def __str__(self):
        return f"NotSoSimpleClass(name={self.name}, count={self.count})"


sc1 = NotSoSimpleClass('test', 10)
print(sc1)
memento = sc1.get_state()
sc1.set_count(20)
print(sc1)
sc2 = NotSoSimpleClass()
sc2.restore_state(memento)
print(sc2)
