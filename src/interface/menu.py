import pygame


class menu():
    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))

    def button_clicked(self, button_pos, button_size, click_pos):
        if (button_pos[0] <= click_pos[0] <= button_pos[0] + button_size[0]):
            if (button_pos[1] <= click_pos[1] <= button_pos[1] + button_size[1]):
                return True
        return False
