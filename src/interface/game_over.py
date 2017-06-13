import pygame


class game_over():
    def __init__(self, view):
        self.resources = {}
        self.display = view
        self.screen_size = view.get_screen_settings()['size']
        self.resources['game_over_msg'] = pygame.image.load('../resources/game_over_msg.png')
        self.resources['game_over_char'] = pygame.image.load('../resources/dino_dead.png')
        self.resources['press_enter'] = pygame.image.load('../resources/press_enter.png')
        self.resources['save_msg'] = pygame.image.load('../resources/save_msg.png')
        self.resources['game_over_pos'] = (self.screen_size[0] * 0.4,
                                           self.screen_size[1] * 0.45)
        self.resources['game_over_size'] = self.get_size(self.resources['game_over_msg'])
        self.resources['press_enter_pos'] = (self.screen_size[0] * 0.37,
                                             self.screen_size[1] * 0.65)
        self.resources['save_msg_pos'] = (self.resources['press_enter_pos'][0],
                                          self.resources['press_enter_pos'][1] + 50)

    def show(self):
        """
        Shows the game over panel.
        """
        self.display.set_screen_caption('Game Over')
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    return (True, "main_menu", None)
                if (event.key == pygame.K_s):
                    return (True, "save_progress", None)
            if (event.type == pygame.QUIT):
                return (False, '', None)

        self.display.display_single_image(self.resources['game_over_msg'],
                                          self.resources['game_over_pos'])
        self.display.display_single_image(self.resources['game_over_char'],
                                          self.resources['game_over_pos'])
        self.display.display_single_image(self.resources['press_enter'],
                                          self.resources['press_enter_pos'])
        self.display.display_single_image(self.resources['save_msg'],
                                          self.resources['save_msg_pos'])
        return (True, 'game_over', None)

    def get_size(self, img):
        x = img.get_width()
        y = img.get_height()
        return (x, y)
