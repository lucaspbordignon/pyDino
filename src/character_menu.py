import pygame
from menu import menu


class character_menu(menu):
    def __init__(self, view, char_types):
        self.display = view
        self.char_types = char_types
        self.extra = [None, None]

    def show(self):
        """
        Shows the character menu. The options of characters will be
        displayed and the use can select which of them he wants to play
        with. If not selected, the system must stay at this state.
        """
        # Setup
        self.display.set_screen_caption('Choose Character')
        last_mouse_click = (-1, -1)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return (False, '', None)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                last_mouse_click = pygame.mouse.get_pos()

        # Check if a char was selected
        selected, char = self.check_selected(last_mouse_click)
        if (selected):
            self.extra[0] = char

        selected, level = self.check_level_selected(last_mouse_click)
        if (selected):
            self.extra[1] = level
            
        if (None not in self.extra):
            return (True, 'start_match', self.clear())

        # If no action was taken
        return (True, 'choose_char', None)

    def check_selected(self, last_click):
        """
        Checks if a character was selected, based on the char size and
        position. Returns the result and the type, if selected.
        """
        for char in self.char_types.values():
            self.display.display_single_image(char.get_image(),
                                              char.get_position())
            if (self.button_clicked(char.get_position(),
                                    char.get_size(),
                                    last_click)):
                return (True, char)
        return (False, '')

    def check_level_selected(self, last_click):
        position = (40, 40)
        for i in range(1, 3):
            img = self.display.resources['numbers'][str(i)]
            size = (img.get_width(), img.get_height())
            self.display.display_single_image(img, position)

            if (self.button_clicked(position,
                                    size,
                                    last_click)):
                return (True, i)
            position = (position[0] + size[0] + 5, position[1])
        return (False, None)

    def clear(self):
        backup = self.extra
        self.extra = [None, None]
        return backup
