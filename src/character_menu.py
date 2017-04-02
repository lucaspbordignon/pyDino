import pygame
from dino import dino


class character_menu():
    def __init__(self, surface, screen_settings):
        self.resources = {}
        self.dino_params = {}
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        self.resources['ground'] = self.load_image('ground.png')
        self.dino_params['type'] = 0
        self.dino_params['pos'] = (100, 350)
        self.dino_params['size'] = (44, 47)
        self.dino_params['name'] = ''

    def show(self):
        # Setup
        pygame.display.set_caption(self.caption + ': Choose Character')
        self.last_mouse_click = (-1, -1)
        # Default type
        self.dino = dino(self.dino_params)
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '', None)
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.last_mouse_click = pygame.mouse.get_pos()

            # Selected Char
            if (self.button_clicked(self.dino_params['pos'], self.dino_params['size'],
                                    self.last_mouse_click)):
                self.last_mouse_click = (-1, -1)
                return (1, 'start_match', self.dino)

            # Default background
            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))

            self.screen.blit(self.dino.get_image(), self.dino.get_position())

            # Updates the game display
            pygame.display.flip()

    def button_clicked(self, button_pos, button_size, click_pos):
        if (button_pos[0] <= click_pos[0] <= button_pos[0] + button_size[0]):
            if (button_pos[1] <= click_pos[1] <= button_pos[1] + button_size[1]):
                return True
        return False

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
