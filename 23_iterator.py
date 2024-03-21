class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.data):
            val = self.data[self.idx]
            self.idx += 1
            return val
        else:
            raise StopIteration


class CustomClass:
    def __init__(self, data):
        self.data = data

    # iterable class
    def __iter__(self):
        return CustomIterator(self.data)


data = [i for i in range(10)]
cc = CustomClass(data)

for d in cc:
    print(d)
