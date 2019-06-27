from models.simple_physics_car import SimplePhysicsCar


class SimpleRotationCar(SimplePhysicsCar):

    x = 10
    y = 200
    old_x = 10
    old_y = 200
    rot = 0

    def move(self, delta_t=0):
        super().move(delta_t)
        rot = ((self.y - self.old_y) / (self.x - self.old_x)) * -1
        # print(rot)
