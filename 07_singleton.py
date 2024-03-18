class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
            # print("Creating Singleton instance")
        return class_._instance


class MyClass(Singleton):
    pass


x = MyClass()
y = MyClass()

print(x == y)
