from models.car import Car


class SimplePhysicsCar(Car):
    def __init__(self):
        super().__init__(10, 200)

    def move(self, delta_t=0):
        # if not self.pause:
        #     self.x = self.x + 1000000000 * delta_t
        #     self.y = self.y
        self.x = self.x + 1
        self.y = self.y + 0
