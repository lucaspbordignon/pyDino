import pygame


class coin():
    def __init__(self, position, value=1):
        self.__image = pygame.image.load('../resources/coin.png')
        self.__position = position
        self.__value = value

    def get_position(self):
        return self.__position

    def get_size(self):
        return (self.__image.get_width(), self.__image.get_height())

    def get_image(self):
        return self.__image

    def value(self):
        return self.__value

    def set_position(self, value):
        self.__position = value

    def hitted(self, char_pos, char_size):
        coin_pos = self.get_position()
        coin_size = self.get_size()
        if (coin_pos[0] <= char_pos[0] + char_size[0] <= coin_pos[0] + coin_size[0]):
            if (coin_pos[1] <= char_pos[1] <= coin_pos[1] + coin_size[1]):
                return True
        return False
