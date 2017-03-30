import pygame


class match():
    def __init__(self, surface, screen_settings, dino, selected_map='default'):
        self.resources = {}
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        self.resources['ground'] = self.load_image('ground.png')
        self.dino = dino
        self.map = selected_map

    def start(self):
        # Setup
        pygame.display.set_caption(self.caption + ': Playing')
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        actual_pos = self.dino.get_position()
                        new_pos = (actual_pos[0], actual_pos[1] - 5)
                        self.dino.set_position(new_pos)

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))

            self.screen.blit(self.dino.get_image(), self.dino.get_position())
            # Updates the game display
            pygame.display.flip()

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
