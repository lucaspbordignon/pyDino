from main_menu import main_menu
from character_menu import character_menu
from match import match
from game_over import game_over
from view import view


class game_runner():
    """
        Class used to run an instace of the game. This class controls all the
    game, including transitions among the different scenes and menus.
    """
    def __init__(self):
        self.actual_scene = 'main_menu'
        self.game_running = 1
        self.display = view()

    def main_menu(self):
        menu = main_menu(self.screen, self.screen_settings)
        self.game_running, self.actual_scene = menu.show()

    def choose_char(self):
        char_menu = character_menu(self.screen, self.screen_settings)
        self.game_running, self.actual_scene, self.dino = char_menu.show()

    def start_match(self):
        new_match = match(self.screen, self.screen_settings, self.dino)
        self.game_running, self.actual_scene = new_match.start()

    def game_over(self):
        gameOver = game_over(self.screen, self.screen_settings)
        self.game_running, self.actual_scene = gameOver.show()

    def run(self):
        while self.game_running:
            self.game_running, self.actual_scene = self.display.show(self.actual_scene)
