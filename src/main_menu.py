import pygame
from menu import menu


class main_menu(menu):
    # TODO:
    # - Receive the object 'view' as parameter, to avoid calling the blit() here
    def __init__(self, screen, screen_settings):
        # Setup
        self.screen = screen
        self.screen_settings = screen_settings

        # Resources
        self.buttons = {}
        position = (40, 40)
        img = self.load_image('new_game_button.png')
        size = (img.get_width(), img.get_height())
        self.buttons['new_game'] = (position, size, img)

    def show(self):
        # Setup
        pygame.display.set_caption(self.screen_settings['caption'] +
                                   ': Main Menu')
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
        button_pos, button_size, button_img = self.buttons[button]
        if (self.button_clicked(button_pos, button_size, last_click)):
            return True
        self.screen.blit(button_img, button_pos)
        return False
