import pygame


class game_over():
    def __init__(self, surface, screen_settings):
        self.resources = {}
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        self.resources['ground'] = pygame.image.load('../resources/ground.png')
        self.game_over_pos = (self.screen_size[0] * 0.4, self.screen_size[1] * 0.5)
        self.game_over_size = (159, 29)

    def blit_images(self):
        self.screen.fill(self.background_color)
        self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))
        self.screen.blit(pygame.image.load('../resources/game_over_msg.png'), self.game_over_pos)
        self.screen.blit(pygame.image.load('../resources/dino_dead.png'), self.game_over_pos)
        pygame.display.flip()

    def show(self):
        pygame.display.set_caption(self.caption + ': Game Over')
        self.last_mouse_click = (-1, -1)
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '')
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.last_mouse_click = pygame.mouse.get_pos()
            self.blit_images()

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
