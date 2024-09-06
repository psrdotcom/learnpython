"""Classes of Python"""


class Car(object):
    """Car Class"""

    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def describe(self):
        """describe function"""
        print(self.name + ' has ' + str(self.wheels) + ' wheels')


my_car = Car('Skoda', 4)
my_another_car = Car('RangeRover', 4)

my_car.describe()

my_another_car.describe()
