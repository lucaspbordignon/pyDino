import pygame
from interface.main_menu import main_menu
from interface.character_menu import character_menu
from interface.game_over import game_over
from interface.login import login


class view():
    def __init__(self, char_types):
        self.resources = {}
        self.screen_settings = {}
        self.screen_settings['size'] = (960, 440)
        self.screen_settings['color'] = (250, 250, 250)
        self.screen_settings['caption'] = 'pyDino'

        # Displays the window
        self.screen = pygame.display.set_mode(self.screen_settings['size'])
        pygame.display.set_caption(self.screen_settings['caption'])

        # Resources
        self.load_media()

        # Utilities
        self.screen_settings['ground_threshold'] = (
            self.resources['ground_pos'][1] + self.resources['ground'].get_height() / 2
        )

        # Menus
        self.menus = {
            'main_menu': main_menu(self),
            'choose_char': character_menu(self, char_types),
            'game_over': game_over(self),
            'login': login()
        }

    def get_screen_settings(self):
        return self.screen_settings

    def set_screen_caption(self, caption):
        pygame.display.set_caption(self.screen_settings['caption'] +
                                   ': ' + caption)

    def show_menu(self, actual_scene='main_menu'):
        """
        Shows one of the system menus, passed by parameter
        """
        self.clear()
        running, actual_scene, extra = self.menus[actual_scene].show()
        return running, actual_scene, extra

    def load_media(self):
        """
        Loads all the images used.
        """
        self.resources['ground'] = pygame.image.load('../resources/ground.png')
        self.resources['ground_pos'] = (0, self.screen_settings['size'][1] - 30)
        numbers = {str(i): pygame.image.load('../resources/' + str(i) + '.png')
                   for i in range(10)}
        self.resources['numbers'] = numbers
        self.resources['difficulty'] = pygame.image.load('../resources/difficulty.png')

    def display_images(self, list):
        """
        Receives a list and call the pygame.blit() function over all the
        elements of it.
        The elements of the list must contain the get_image() and
        get_position() methods.
        """
        for obj in list:
            self.screen.blit(obj.get_image(), obj.get_position())

    def display_single_image(self, image, pos):
        """
        Displays just one image at the given position.
        """
        self.screen.blit(image, pos)

    def display_int(self, value, position):
        """
        Displays an integer, using images, inside the frame at the given
        position.
        """
        value = str(value)
        if (len(value) < 2):
            images = (self.resources['numbers']['0'],
                      self.resources['numbers'][value])
        else:
            images = (self.resources['numbers'][value[0]],
                      self.resources['numbers'][value[1]])
        position = (position, (position[0] + images[0].get_width(), position[1]))

        self.screen.blit(images[0], position[0])
        self.screen.blit(images[1], position[1])

    def update(self):
        """
        Just update the pygame screen.
        """
        pygame.display.flip()

    def clear(self):
        """
        Clear the pygame screen and insert the ground image on it.
        """
        self.screen.fill(self.screen_settings['color'])
        self.screen.blit(self.resources['ground'],
                         self.resources['ground_pos'])
