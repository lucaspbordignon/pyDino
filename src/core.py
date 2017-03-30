import pygame
from main_menu import main_menu
from character_menu import character_menu


class game_runner():
    """
        Class used to run an instace of the game. This class controls all the
    game, including transitions among the different scenes and menus.
    """
    def __init__(self):
        self.scenes = {
            'main_menu': self.main_menu,
            'choose_char': self.choose_char,
        }
        self.actual_character = {}
        self.screen_settings = {}
        self.screen_settings['size'] = (960, 440)
        self.screen_settings['color'] = (250, 250, 250)
        self.screen_settings['caption'] = 'pyDino'
        # Initial setup
        self.actual_scene = 'main_menu'
        self.game_running = 1

    def main_menu(self):
        menu = main_menu(self.screen, self.screen_settings)
        self.game_running, self.actual_scene = menu.show()

    def choose_char(self):
        char_menu = character_menu(self.screen, self.screen_settings)
        self.game_running, self.actual_scene, self.dino = char_menu.show()

    def run(self):
        # Displays the window
        self.screen = pygame.display.set_mode(self.screen_settings['size'])
        pygame.display.set_caption(self.screen_settings['caption'])

        while self.game_running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return 0

            # Calls the right menu to be executed
            self.scenes[self.actual_scene]()
