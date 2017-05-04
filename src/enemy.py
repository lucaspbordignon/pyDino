import pygame


class enemy():
    def __init__(self, screen_size, ground_threshold, media_name='cactus.png'):
        self._image = pygame.image.load('../resources/' + media_name)
        self._size = (self._image.get_width(), self._image.get_height())
        self._position = (screen_size[0], ground_threshold - self._size[1])
        self._hitted = False

    def get_position(self):
        return self._position

    def get_image(self):
        return self._image

    def get_size(self):
        return self._size

    def get_hitted(self):
        return self._hitted

    def set_hitted(self, value):
        self._hitted = value

    def set_position(self, value):
        self._position = value

    def check_hitted(self, object):
        obj_pos = object.get_position()
        obj_size = object.get_size()
        enemy_pos = self.get_position()
        enemy_size = self.get_size()
        if (enemy_pos[0] <= obj_pos[0] + obj_size[0] <= enemy_pos[0] + enemy_size[0]):
            if (obj_pos[1] + obj_size[1] >= enemy_pos[1]):
                return True
        return False
