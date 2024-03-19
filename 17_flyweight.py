import random


class Engine:
    instances = 0

    def __init__(self, identifier, volume, engine_type):
        Engine.instances += 1
        self._identifier = identifier
        self._volume = volume
        self._engine_type = engine_type


class Car:
    def __init__(self, producer, vin, model_name, engine):
        self._producer = producer
        self._vin = vin
        self._model_name = model_name
        self._engine = engine


class CarFactory:
    engines = [Engine('polo', 1.6, 'DIESEL'),
               Engine('poloGTI', 2.0, 'GASOLINE'),
               Engine('golf', 1.5, 'GASOLINE'),
               Engine('e', 0.0, 'ELECTRIC')]

    @staticmethod
    def create_vw_polo(vin):
        return Car('VW', vin, 'Polo', CarFactory.engines[0])

    @staticmethod
    def create_vw_polo_gti(vin):
        return Car('VW', vin, 'Polo GTI', CarFactory.engines[1])

    @staticmethod
    def create_vw_golf(vin):
        return Car('VW', vin, 'Golf', CarFactory.engines[2])

    @staticmethod
    def create_skoda_citigo(vin):
        return Car('Skoda', vin, 'CityGO', CarFactory.engines[3])


def main():
    produced_cars = []
    for i in range(1000):
        engine_type = random.randint(0, 3)
        if engine_type == 0:
            produced_cars.append(CarFactory.create_vw_polo(random.randint(1000000, 99999999)))
        elif engine_type == 1:
            produced_cars.append(CarFactory.create_vw_polo_gti(random.randint(1000000, 9999999)))
        elif engine_type == 2:
            produced_cars.append(CarFactory.create_vw_golf(random.randint(1000000, 9999999)))
        else:
            produced_cars.append(CarFactory.create_skoda_citigo(random.randint(1000000, 9999999)))

    print(f"I created {len(produced_cars)} cars, but only {Engine.instances}, references to Engine objects")


if __name__ == '__main__':
    main()
