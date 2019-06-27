import pygame
import time as time
import pandas as pd

import models

from models.rectangle import Rectangle


# Colors used for drawing with PyGame
WIDTH = 1280
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set to True if the current simulation run should be stored to CSV file
SAVE = False

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Simulation')
clock = pygame.time.Clock()


def save_car_position(tm, x_pos, y_pos):
    """
    Writing the Location and Time to a CSV File
    First creating a Dictionary, which is then converted to a Panda dataframe.
    The dataframe is then stored in data folder with the timestamp of its creation.
    :param tm: List of the time steps
    :param x_pos: x axis position of the car
    :param y_pos: y axis position of the car
    :return:
    """
    d = {'Time': tm, 'xPos': x_pos, 'yPos': y_pos}
    df = pd.DataFrame(d)
    # print(df)
    file_name = "sim_data_{time}.csv".format(time=time.time())
    df.to_csv("data/" + file_name)


def draw_environment(car, rot = 0):
    """Draw the Environment
    Filling the Background with black color.
    Adding a Rectangle which represents the car.
    TODO: Adding Orientation of the Car
    Updating the Frame.
    :param car: The Car Object which is driving in the screen
    :type car: Car
    """
    game_display.fill(BLACK)
    re = Rectangle(200, 200, 100, 50)
    re.rotate(rot)
    re.move(int(car.x,), int(car.y))
    pygame.draw.polygon(game_display, WHITE, re.get_point_list(), 5)
    # print(re.get_point_list())
    # Draw Car with fixed Dimensions
    # pygame.draw.rect(game_display, WHITE, [int(car.x), int(car.y), 50, 20], 2)

    # TODO: Rotate Car to Orientation
    # TODO: Add Vector to Steer
    pygame.display.update()


def main():
    """
    Main function, which initializes the Car Object and starts the Animation Loop.
    Inside the loop the close event and the event of a pressed space key get caught.
    The environment gets drawn.
    The time got stopped.
    The Car gets the request to move.
    :return:
    """
    STOP = False
    my_car = models.SimpleRotationCar()

    time_begin = time.time()

    t = []
    x = []
    y = []

    rot = 0

    while not STOP:
        try:
            time_start = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    STOP = True
                    if SAVE:
                        save_car_position(t, x, y)
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        my_car.pause = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        my_car.pause = False

            draw_environment(my_car, rot)
            rot = rot + 1
            clock.tick(60)

            t.append(time.time() - time_begin)
            my_car.move()
            x.append(my_car.x)
            y.append(my_car.y)
            # time_end = time.time()
            # time_elapsed = time_end - time_start
            # print("Time Elapsed: %10.10f" % time_elapsed)

        except KeyboardInterrupt:
            STOP = True
            # save_car_position(t, x, y)
            pygame.quit()
            quit()


if __name__ == "__main__":
    main()
