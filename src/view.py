import pygame
from main_menu import main_menu
from character_menu import character_menu


class view():
    # TODO:
    # - 'choose_char' deve retornar o tipo de dino selecionado (tratar isso)
    # - Implementar as outras classes

    def __init__(self, char_types):
        self.resources = {}
        self.screen_settings = {}
        self.screen_settings['size'] = (960, 440)
        self.screen_settings['color'] = (250, 250, 250)
        self.screen_settings['caption'] = 'pyDino'

        # Displays the window
        self.screen = pygame.display.set_mode(self.screen_settings['size'])
        pygame.display.set_caption(self.screen_settings['caption'])

        # Resources
        self.resources['ground'] = self.load_image('ground.png')

        # Menus
        self.scenes = {
            'main_menu': main_menu(self.screen, self.screen_settings),
            'choose_char': character_menu(self.screen, self.screen_settings,
                                          char_types),
            #'start_match': self.start_match,
            #'game_over': self.game_over,
        }

        # Initial setup
        self.game_running = 1

    def show(self, actual_scene='main_menu'):
        self.screen.fill(self.screen_settings['color'])
        self.screen.blit(self.resources['ground'],
                         (0, self.screen_settings['size'][1] - 30))

        running, actual_scene = self.scenes[actual_scene].show()
        # Updates the game display
        pygame.display.flip()
        return running, actual_scene

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
