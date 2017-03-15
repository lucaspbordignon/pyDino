from utils import *
import menu_controller


class game_runner():
    def __init__(self):
        self.screen_settings = {}
        self.screen_settings['size'] = (960, 440)
        self.screen_settings['color'] = (250, 250, 250)
        self.screen_settings['caption'] = 'pyDino'

    def run(self):
        # Displays the window
        self.screen = pygame.display.set_mode(self.screen_settings['size'])
        pygame.display.set_caption(self.screen_settings['caption'])
        actual_scene = 'main_menu'
        game_running = 1
        while game_running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return 0

            if (actual_scene == 'main_menu'):
                menu = menu_controller.menu(self.screen, self.screen_settings)
                game_running = menu.show_initial_menu()

            # Updates the game display
            pygame.display.flip()
