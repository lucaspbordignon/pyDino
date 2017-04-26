import pygame
from menu import menu


class character_menu(menu):
    def __init__(self, screen, screen_settings, char_types):
        self.dinos = {}
        self.screen = screen
        self.screen_settings = screen_settings
        self.char_types = char_types

        # Resources
        for char in self.char_types:
            image = self.load_image(str(char) + ".png")
            size = (image.get_width(), image.get_height())
            self.dinos[char] = (size, image)

    def show(self):
        # Setup
        pygame.display.set_caption(self.screen_settings['caption'] +
                                   ': Choose Character')
        last_mouse_click = (-1, -1)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return (0, '', None)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                last_mouse_click = pygame.mouse.get_pos()

        # Check if a char was selected
        for char in self.char_types:
            if (self.button_clicked((0, 0), self.dinos[char][0],
                                    last_mouse_click)):
                last_mouse_click = (-1, -1)
                return (1, 'start_match', char)

            self.screen.blit(self.dinos[char][1], (0, 0))

        # Updates the game display
        pygame.display.flip()
        return (1, 'choose_char')
