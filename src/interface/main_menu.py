import pygame
from interface.menu import menu


class main_menu(menu):
    def __init__(self, view):
        # Setup
        self.display = view

        # Resources
        self.buttons = {}
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
        if (self.show_button(last_mouse_click, 'new_game')):
            return (True, 'choose_char', None)

        # Login button
        if (self.show_button(last_mouse_click, 'login')):
            return (True, 'login', None)

        # Logo
        self.display.display_single_image(self.buttons['pydino'][2],
                                          self.buttons['pydino'][0])

        # Default choice
        return (True, 'main_menu', None)

    def show_button(self, last_click, button):
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
        img = self.load_image('new_game_button.png')
        position = (213, 300)
        size = (img.get_width(), img.get_height())
        self.buttons['new_game'] = (position, size, img)

        img = self.load_image('login_msg.png')
        position = (586, 300)
        size = (img.get_width(), img.get_height())
        self.buttons['login'] = (position, size, img)

        img = self.load_image('pydino.png')
        position = (280, 100)
        size = (img.get_width(), img.get_height())
        self.buttons['pydino'] = (position, size, img)
