import pygame
from menu import menu


class character_menu(menu):
    def __init__(self, screen, screen_settings, char_types):
        self.screen = screen
        self.screen_settings = screen_settings
        self.char_types = char_types

    def show(self):
        """
            Shows the character menu. The options of characters will be
        displayed and the use can select which of them he wants to play
        with. If not selected, the system must stay at this state.
        """
        # Setup
        pygame.display.set_caption(self.screen_settings['caption'] +
                                   ': Choose Character')
        last_mouse_click = (-1, -1)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return (False, '', None)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                last_mouse_click = pygame.mouse.get_pos()

        # Check if a char was selected
        selected, char = self.check_selected(last_mouse_click)
        if (selected):
            return (True, 'start_match', char)

        # If no action was taken
        return (True, 'choose_char', None)

    def check_selected(self, last_click):
        """
            Checks if a character was selected, based on the char size and
        position. Returns the result and the type, if selected.
        """
        for char in self.char_types.values():
            if (self.button_clicked(char.get_position(),
                                    char.get_size(),
                                    last_click)):
                return (True, char)
            self.screen.blit(char.get_image(), char.get_position())
        return (False, '')
