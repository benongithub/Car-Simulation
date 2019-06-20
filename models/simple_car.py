from models.car import Car


class SimpleCar(Car):

    def __init__(self):
        """" Creates Simple Car with Offset"""
        super().__init__(100, 500)

        print("I'm a brand new Simple Car")
