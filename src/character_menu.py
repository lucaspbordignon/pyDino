from utils import *


class character_menu():
    def __init__(self, surface, screen_settings):
        self.resources = {}
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        self.resources['ground'] = load_image('ground.png')

    def show(self):
        # Setup
        pygame.display.set_caption(self.caption + ': Choose Character')
        self.last_mouse_click = (-1, -1)
        char_properties = {}
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '', None)
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.last_mouse_click = pygame.mouse.get_pos()

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))

            # Updates the game display
            pygame.display.flip()
