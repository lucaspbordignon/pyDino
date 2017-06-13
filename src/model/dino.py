import pygame


class dino():
    def __init__(self, position, type, lives=1, smoothness_rate=0.3):
        self.actual_type = type
        self.__image = pygame.image.load('../resources/' + self.actual_type + '.png')
        self.__size = (self.__image.get_width(), self.__image.get_height())
        self.__position = position
        self.__movement = 1
        self.__smoothness_rate = smoothness_rate
        self.__jumping = False
        self.__lives = lives
        self.__coins = 0
        self.__initial_position = position
        self.__initial_lives = lives

    def get_image(self):
        return self.__image

    def get_position(self):
        return self.__position

    def get_movement(self):
        return self.__movement

    def get_size(self):
        return self.__size

    def get_lives(self):
        return self.__lives

    def get_coins(self):
        return self.__coins

    def get_type(self):
        return self.actual_type

    def is_jumping(self):
        return self.__jumping

    def set_position(self, value):
        self.__position = value

    def set_movement(self, value):
        self.__movement = value

    def set_jumping(self, value):
        self.__jumping = value

    def set_lives(self, value, type='default'):
        if (type is 'default'):
            self.__lives = value
        if (type is 'decrement'):
            self.__lives -= value

    def set_coins(self, value, type='default'):
        if (type is 'default'):
            self.__coins = value
        if (type is 'increment'):
            self.__coins += value

    def reset(self):
        self.__position = self.__initial_position
        self.__lives = self.__initial_lives
        self.__coins = 0
        self.__movement = 1

    def jump(self, threshold):
        if (self.__movement):
            self.set_movement(self.__movement - self.__smoothness_rate)
        if (self.get_position()[1] + self.get_size()[1] >= threshold):
            self.set_movement(0)
            self.set_jumping(False)
            self.set_position((self.get_position()[0],
                               threshold - self.get_size()[1] - 1))
        else:
            self.set_position((self.get_position()[0],
                               self.get_position()[1] - self.get_movement()))
