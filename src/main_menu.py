import pygame
from menu import menu


class main_menu(menu):
    def __init__(self, screen, screen_settings):
        # Setup
        self.screen = screen
        self.screen_settings = screen_settings
        # Resources
        self.buttons = {}
        position = (39, 40)
        size = (158, 29)
        self.buttons['new_game'] = (position, size, self.load_image('new_game_button.png'))

    def show(self):
        # Setup
        pygame.display.set_caption(self.screen_settings['caption'] +
                                   ': Main Menu')
        last_mouse_click = (-1, -1)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return (0, '')
            if (event.type == pygame.MOUSEBUTTONDOWN):
                last_mouse_click = pygame.mouse.get_pos()

        # New game button
        new_game_pos, new_game_size, new_game_img = self.buttons['new_game']
        if (self.button_clicked(new_game_pos, new_game_size, last_mouse_click)):
            last_mouse_click = (-1, -1)
            return (1, 'choose_char')

        self.screen.blit(new_game_img, new_game_pos)
        return (1, 'main_menu')
