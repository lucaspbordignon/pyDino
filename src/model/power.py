import pygame


class power():
    def __init__(self, position=(-100, -100), moving=False):
        self.__image = pygame.image.load('../resources/power.png')
        self.__size = (self.__image.get_width(), self.__image.get_height())
        self.__pos = position
        self.__moving = moving

    def get_image(self):
        return self.__image

    def get_position(self):
        return self.__pos

    def get_size(self):
        return self.__size

    def set_position(self, value):
        self.__pos = value

    def move(self, velocity=4):
        x_power, y_power = self.__pos
        self.__pos = (x_power + velocity, y_power)
