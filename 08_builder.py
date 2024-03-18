class Cook:
    """
    Director - manages the creation of the object
    """

    def __init__(self):
        self._builder = None

    def prepare(self, builder):
        self._builder = builder
        self._builder.prepare_dough()
        self._builder.add_extras()
        self._builder.bake()


class PizzaBuilder:
    """
    Builder - abstract interface for creating target objects
    """

    def __init__(self):
        self.pizza = Pizza()

    def prepare_dough(self):
        pass

    def add_extras(self):
        pass

    def bake(self):
        pass


class MargeritaPizzaBuilder(PizzaBuilder):
    """
    ConcreteBuilder - a specific builder that creates object
    """

    def prepare_dough(self):
        print("Preparing dough for margerita pizza")

    def add_extras(self):
        print("Adding extras to margerita pizza")

    def bake(self):
        print("Baking margerita pizza")


class PepperoniPizzaBuilder(PizzaBuilder):
    """
    ConcreteBuilder - a specific builder that creates object
    """

    def prepare_dough(self):
        print("Preparing dough for pepperoni pizza")

    def add_extras(self):
        print("Adding extras to pepperoni pizza")

    def bake(self):
        print("Baking pepperoni pizza")


class Pizza:
    """
    generated complex object
    """
    pass


cook = Cook()

my_choose = PepperoniPizzaBuilder()
cook.prepare(my_choose)
pizza = my_choose.pizza

my_second_choose = MargeritaPizzaBuilder()
cook.prepare(my_second_choose)
second_pizza = my_second_choose.pizza
