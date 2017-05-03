from view import view
from dino import dino


class game_runner():
    """
        Class used to run an instace of the game. This class controls all the
    game, including transitions among the different scenes and menus.
    """
    def __init__(self):
        self.char_types = {
            'default': dino((0, 0), 'default')
        }
        self.actual_scene = 'main_menu'
        self.game_running = True
        self.display = view(self.char_types, None)
        self.extra = None

    def run(self):
        """
            Where all the magic happens. Connects the view with the model.
        Runs the game.
        """
        while self.game_running:
            (self.game_running, self.actual_scene) = self.display.show(self.actual_scene)
