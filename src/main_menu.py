import pygame
from menu import menu


class main_menu(menu):
    def __init__(self, view):
        # Setup
        self.display = view

        # Resources
        self.load_media()

    def show(self):
        # Setup
        self.display.set_screen_caption('Main Menu')
        last_mouse_click = (-1, -1)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return (False, '', None)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                last_mouse_click = pygame.mouse.get_pos()

        # New game button
        if (self.show_button(last_mouse_click)):
            return (True, 'choose_char', None)

        # Default choice
        return (True, 'main_menu', None)

    def show_button(self, last_click, button='new_game'):
        """
        Shows a given button and return True if there's a mouse click on it
        """
        button_pos, button_size, button_img = self.buttons[button]
        self.display.display_single_image(button_img, button_pos)
        if (self.button_clicked(button_pos, button_size, last_click)):
            return True
        return False

    def load_media(self):
        """
        Load all images and set it positions
        """
        self.buttons = {}
        position = (40, 40)
        img = self.load_image('new_game_button.png')
        size = (img.get_width(), img.get_height())
        self.buttons['new_game'] = (position, size, img)
