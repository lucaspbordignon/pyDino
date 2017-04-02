import pygame


class match():
    def __init__(self, surface, screen_settings, dino, selected_map='default'):
        self.resources = {}
        self.ground = {}
        # Frame
        self.clock = pygame.time.Clock()
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        # Media
        self.resources['ground'] = self.load_image('ground.png')
        self.resources['cactus'] = self.load_image('cactus.png')
        # General
        self.ground['size'] = (1200, 30)
        self.ground['pos'] = (0, self.screen_size[1] - self.ground['size'][1])
        self.dino = dino
        self.map = selected_map
        self.smoothness_rate = 1e-1

    def start(self):
        # Setup
        pygame.display.set_caption(self.caption + ': Playing')
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '')
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_UP and
                            not self.dino.is_jumping()):
                        self.dino.set_movement(5)
                        self.dino.set_jumping(True)

                    if (event.key == pygame.K_DOWN):
                        self.dino.set_movement(-5)

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], self.ground['pos'])

            # Movement
            dino_movement = self.dino.get_movement()
            new_movement_rate = dino_movement - (self.smoothness_rate)
            self.dino.set_movement(new_movement_rate)

            # Ground
            actual_pos = self.ground_threshold()

            # Recalculates the dino pos
            new_pos = (actual_pos[0], actual_pos[1] - self.dino.get_movement())
            self.dino.set_position(new_pos)

            self.screen.blit(self.dino.get_image(), self.dino.get_position())
            self.screen.blit(self.resources['cactus'], (100, 100))

            # Updates the game display
            pygame.display.flip()
            self.clock.tick(60)

    def ground_threshold(self):
        ground_pos = self.ground['pos']
        ground_size = self.ground['size']
        dino_pos = self.dino.get_position()
        dino_size = self.dino.get_size()
        if (dino_pos[1] + dino_size[1] >= ground_pos[1] + ground_size[1] / 2):
            self.dino.set_movement(0)
            dino_pos = (dino_pos[0], ground_pos[1] + (ground_size[1] / 2) - (dino_size[1] + 1))
            self.dino.set_jumping(False)
        return dino_pos

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
