# TODO: změnit na abstraktní třídy

class Drink:
    def get_volume(self):
        pass

    def is_addictive(self):
        pass

    def get_number_of_sugar_lumps(self):
        pass

    def get_taste(self):
        pass


class Coffee(Drink):
    def get_volume(self):
        return "150ml"

    def is_addictive(self):
        return True

    def get_number_of_sugar_lumps(self):
        return 0

    def get_taste(self):
        return "bitter"


class Tea(Drink):
    def get_volume(self):
        return "250ml"

    def is_addictive(self):
        return False

    def get_number_of_sugar_lumps(self):
        return 2

    def get_taste(self):
        return "sweet"


class DrinkPurchase:
    def buy(self):
        pass


class CoffeePurchase(DrinkPurchase):

    def __init__(self):
        self._coffee = Coffee()

    def buy(self, cost):
        print(f"Buying a coffee for {cost}")
        return self._coffee

    def sell(self, volume):
        print(f"Selling a coffee of {volume} volume")
        return self._coffee


class TeaPurchase(DrinkPurchase):
    def __init__(self):
        self._tea = Tea()

    def buy(self, cost):
        print(f"Buying a tea for {cost}")
        return self._tea


def main():
    #coffee = Coffee()
    #tea = Tea()

    coffee_purchase = CoffeePurchase()
    coffee_purchase.buy(200)
    tea_purchase = TeaPurchase()
    tea_purchase.buy(150)


if __name__ == '__main__':
    main()
