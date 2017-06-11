from interface.view import view
from model.dino import dino
from model.match import match


class game_runner():
    """
        Class used to run an instace of the game. This class controls all the
    game, including transitions among the different scenes and menus.
    """
    def __init__(self):
        self.char_types = {
            'default': dino((100, 350), 'default')
        }
        self.display = view(self.char_types)
        self.actual_scene = 'main_menu'
        self.game_running = True
        self.match = None
        self.extra = None

    def run(self):
        """
            Where all the magic happens. Connects the view with the model.
        Runs the game.
        """
        while self.game_running:
            self.display.clear()
            if (self.actual_scene == 'start_match'):
                if (self.extra is not None):
                    self.match = match(self.display.get_screen_settings(), self.extra)
                    self.actual_scene = 'match_running'
                    self.display.set_screen_caption('Playing')

            if (self.actual_scene == 'match_running'):
                    (self.game_running, self.actual_scene, self.extra) = self.match.run()
                    if (self.extra is not None):
                        # Show lives and coins
                        self.display.display_int(self.extra.pop('lives'), (40, 40))
                        self.display.display_int(self.extra.pop('coins'), (150, 40))

                        # Display the game objects
                        self.display.display_images(self.extra)
            else:
                (self.game_running,
                 self.actual_scene,
                 self.extra) = self.display.show_menu(self.actual_scene)

            self.display.update()
