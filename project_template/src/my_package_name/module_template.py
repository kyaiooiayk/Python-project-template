import abc


class Vehicle(metaclass=abc.ABCMeta):
    # These are two class attribute that depends on the type of object
    base_sale_price = 0.0
    wheels = 0

    def __init__(self, miles, make, model, year):
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year

    def sale_price(self):
        """
        We charge a flat rate of 5k per wheels
        """
        return 5000.0 * self.wheels

    def purchaise_price(self):
        """
        We buy back according to the miles the car has
        """
        return self.base_sale_price - (0.1 * self.miles)

    @abc.abstractmethod
    def vehicle_type(self):
        """
        Returns a string representing the type of vehicle this is.
        This will be defined in the derived class
        """
        pass


class Car(Vehicle):
    # Class attributes specific to the Car class
    wheels = 4
    based_sale_price = 8000

    def vehicle_type(self):
        """
        Returns a string representing the type of vehicle this is.
        """
        return "car"


class Motorcycle(Vehicle):
    # Class attributes specific to the Car class
    wheels = 2
    based_sale_price = 4000

    def vehicle_type(self):
        """
        Returns a string representing the type of vehicle this is.
        """
        return "motorcycle"
