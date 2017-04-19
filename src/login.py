import pygame

class login():
    def __init(self, surface, screen_seetings):
        self.resources = {}
        self.screen = surface
        self.screen_size = screen_seetings['size']
        self.background_color = screen_seetings['color']
        self.caption = screen_seetings['caption']
        self.resources['ground'] = self.load_image('ground.png')

    def show(self):
        pygame.display.set_caption(self.caption + ': Login')
        self.last_mouse_click = (-1, -1)
        login_name_pos = (self.screen_size[0]*0.45, self.screen_size[1]*0.35)
        login_pass_pos = (self.screen_size[0]*0.45, self.screen_size[1]*0.7)
        login_size = (0, 0)
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                return (0, '')
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.last_mouse_click = pygame.mouse.get_pos()

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))

            pygame.display.flip()

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
