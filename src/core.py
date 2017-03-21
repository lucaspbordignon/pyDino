from utils import *
import menu_controller


class game_runner():
    """
        Class used to run an instace of a game. This class controls all the
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
        menu = menu_controller.menu(self.screen, self.screen_settings)
        self.game_running, self.actual_scene = menu.show_initial_menu()

    def choose_char(self):
        menu = menu_controller.menu(self.screen, self.screen_settings)
        self.game_running, self.actual_scene, props = menu.show_choose_char()
        if (props is not None):
            self.actual_character['name'] = props['name']

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
