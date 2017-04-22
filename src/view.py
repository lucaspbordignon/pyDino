import pygame
from main_menu import main_menu


class view():
    def __init__(self):
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
            'choose_char': self.choose_char,
            'start_match': self.start_match,
            'game_over': self.game_over,
        }

        # Initial setup
        self.game_running = 1

    def show(self, scene='main_menu'):
        self.screen.fill(self.screen_settings['color'])
        self.screen.blit(self.resources['ground'],
                         (0, self.screen_settings['size'][1] - 30))

        running, actual_scene = self.scenes[scene].show()
        # Updates the game display
        pygame.display.flip()
        return running, actual_scene
