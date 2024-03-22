"""
Task 3 - Abstract Factory

Write a program in which two Abstract Car Factories (left and right hand drive)
produce 3 types of cars (sedan, station wagon, coupe).
"""


class Sedan:
    def build(self):
        pass


class SedanLeftHandDrive(Sedan):
    def build(self):
        print("Sedan - left hand drive")


class SedanRightHandDrive(Sedan):
    def build(self):
        print("Sedan - right hand drive")


class StationWagon:
    def build(self):
        pass


class StationWagonLeftHandDrive(StationWagon):
    def build(self):
        print("Station wagon - left hand drive")


class StationWagonRightHandDrive(StationWagon):
    def build(self):
        print("Station wagon - right hand drive")


class Coupe:
    def build(self):
        pass


class CoupeLeftHandDrive(Coupe):
    def build(self):
        print("Coupe - left hand drive")


class CoupeRightHandDrive(Coupe):
    def build(self):
        print("Coupe - left hand drive")


class CarFactory:
    def build_sedan(self):
        pass

    def build_wagon_station(self):
        pass

    def build_coupe(self):
        pass


class CarFactoryLeftHandDrive(CarFactory):
    def build_sedan(self):
        return SedanLeftHandDrive()

    def build_wagon_station(self):
        return StationWagonLeftHandDrive()

    def build_coupe(self):
        return CoupeLeftHandDrive()


class CarFactoryRightHandDrive(CarFactory):
    def build_sedan(self):
        return SedanRightHandDrive()

    def build_wagon_station(self):
        return StationWagonRightHandDrive()

    def build_coupe(self):
        return CoupeRightHandDrive()


def main():
    select_car_factory = input("Select car factory [Left hand|Right hand]: ")
    car_factory = None
    if select_car_factory == "L":
        car_factory = CarFactoryLeftHandDrive()
    else:
        car_factory = CarFactoryRightHandDrive()

    if car_factory is not None:
        select_car_type = input("Select car type [Sedan|Wagon|Coupe]: ")
        my_car = None
        if select_car_type == "S":
            my_car = car_factory.build_sedan()
        elif select_car_type == "W":
            my_car = car_factory.build_wagon_station()
        elif select_car_type == "C":
            my_car = car_factory.build_coupe()

        if my_car is not None:
            my_car.build()


if __name__ == "__main__":
    main()
