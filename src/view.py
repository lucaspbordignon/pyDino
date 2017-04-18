import pygame

class view():
    def __init__(self):
        self.screen_settings = {}
        self.screen_settings['size'] = (960, 440)
        self.screen_settings['color'] = (250, 250, 250)
        self.screen_settings['caption'] = 'pyDino'

        # Displays the window
        self.screen = pygame.display.set_mode(self.screen_settings['size'])
        pygame.display.set_caption(self.screen_settings['caption'])

        # Initial setup
        self.game_running = 1

    def show(self):
        while self.game_running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return 0

            # Updates the game display
            pygame.display.flip()
