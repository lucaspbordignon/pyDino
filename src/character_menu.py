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
        actual_dino_type = 0
        dino_pos = (100, 350)
        char_types = {
            0: 'default',
        }
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '', None)
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.last_mouse_click = pygame.mouse.get_pos()

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))

            dino_img = self.load_dino_img(char_types[actual_dino_type])
            self.screen.blit(dino_img, dino_pos)

            # Updates the game display
            pygame.display.flip()

    def load_dino_img(self, dino_type):
        img = load_image(str(dino_type) + '.png')
        return img
