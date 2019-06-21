class Car:
    pause = False
    orientation = 0
    steering = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, delta_t = 0):
        self.x = self.x
        self.y = self.y
