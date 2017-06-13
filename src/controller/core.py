from interface.view import view
from model.dino import dino
from model.match import match
from model.database import database


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
        self.database = database()
        self.actual_scene = 'main_menu'
        self.game_running = True
        self.username = None
        self.dino = None
        self.match = None
        self.extra = None

    def run(self):
        """
            Where all the magic happens. Connects the view with the model.
        Runs the game.
        """
        while self.game_running:
            self.display.clear()
            if (self.actual_scene == 'login'):
                (self.game_running,
                 self.actual_scene,
                 self.username) = self.display.show_menu(self.actual_scene)

            if (self.actual_scene == 'main_menu'):
                if self.dino:
                    self.dino.reset()
                (self.game_running,
                 self.actual_scene,
                 self.extra) = self.display.show_menu(self.actual_scene)

            if (self.actual_scene == 'save_progress'):
                self.database.create_table()
                self.database.add({'name': self.username,
                                   'password': '',
                                   'type': self.dino.get_type(),
                                   'coins': self.dino.get_coins()})
                self.actual_scene = 'main_menu'

            if (self.actual_scene == 'start_match'):
                self.start_match()

            if (self.actual_scene == 'match_running'):
                self.running_match()

            else:
                (self.game_running,
                 self.actual_scene,
                 self.extra) = self.display.show_menu(self.actual_scene)

            self.display.update()
        self.database.close()

    def start_match(self):
        """
            Starts a new empty match.
        """
        if (self.extra is not None):
            self.match = match(self.display.get_screen_settings(), self.extra)
            self.actual_scene = 'match_running'
            self.display.set_screen_caption('Playing')
            self.dino = self.match.get_dino()

    def running_match(self):
        """
            Keeps the match running, updating the pictures and all the related
            objects.
        """
        (self.game_running, self.actual_scene, self.extra) = self.match.run()

        if (self.extra is not None):
            # Show lives and coins
            self.display.display_int(self.extra.pop('lives'), (40, 40))
            self.display.display_int(self.extra.pop('coins'), (150, 40))

            # Power
            self.display.display_images(self.extra.pop('power'))

            # Display the game objects
            self.display.display_images(list(self.extra.values()))
