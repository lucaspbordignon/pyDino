import pygame
from main_menu import main_menu
from character_menu import character_menu
from match import match


class view():
    # TODO:
    # - 'start_match' deve receber um personagem pra começar o jogo
    # - Implementar as outras classes

    def __init__(self, char_types, extra=None):
        self.resources = {}
        self.screen_settings = {}
        self.screen_settings['size'] = (960, 440)
        self.screen_settings['color'] = (250, 250, 250)
        self.screen_settings['caption'] = 'pyDino'

        # Displays the window
        self.screen = pygame.display.set_mode(self.screen_settings['size'])
        pygame.display.set_caption(self.screen_settings['caption'])

        # Resources
        self.resources['ground'] = pygame.image.load('../resources/ground.png')

        # Menus
        self.scenes = {
            'main_menu': main_menu(self.screen, self.screen_settings),
            'choose_char': character_menu(self.screen, self.screen_settings,
                                          char_types),
            'start_match': match(self.screen, self.screen_settings, None),
            #'game_over': self.game_over,
        }

        # Initial setup
        self.extra = extra

    def show(self, actual_scene='main_menu'):
        self.screen.fill(self.screen_settings['color'])
        self.screen.blit(self.resources['ground'],
                         (0, self.screen_settings['size'][1] - 30))

        running, actual_scene, self.extra = self.scenes[actual_scene].show()
        # Updates the game display
        pygame.display.flip()

        return running, actual_scene
