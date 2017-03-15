from utils import *


class menu():
    def __init__(self, surface, screen_settings):
        self.resouces = {}
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        self.resouces['ground'] = load_image('ground.png')

    def show_initial_menu(self):
        pygame.display.set_caption(self.caption + ': Main Menu')
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return 0

            self.screen.fill(self.background_color)
            self.screen.blit(self.resouces['ground'], (0, self.screen_size[1] - 30))
            # Updates the game display
            pygame.display.flip()
        return 1
