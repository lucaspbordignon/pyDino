import pygame
from model.enemy import enemy
from model.prize import prize
from model.power import power


class match():
    def __init__(self, screen_settings, extra):
        self.ground = {}
        # Frame
        self.clock = pygame.time.Clock()
        self.screen_size = screen_settings['size']
        self.ground_limit = screen_settings['ground_threshold']

        # Media
        self.resources = self.load_media()

        # General
        ground_x = self.resources['ground'].get_width()
        ground_y = self.resources['ground'].get_height()
        self.ground['size'] = (ground_x, ground_y)
        self.ground['pos'] = (0, self.screen_size[1] - ground_y)
        self.dino = extra[0]
        self.enemy = enemy(self.screen_size, self.ground_limit)
        self.prize = prize((self.screen_size[0], self.screen_size[1] - 170))
        self.powers = []
        self.difficulty = extra[1]

    def run(self):
        # Setup
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return (False, '', None)
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP and not self.dino.is_jumping()):
                    self.dino.set_movement(8)
                    self.dino.set_jumping(True)
                if (event.key == pygame.K_DOWN):
                    self.dino.set_movement(-5)
                if (event.key == pygame.K_h):
                    if self.dino.get_coins() > 4:
                        self.dino.set_coins(self.dino.get_coins() - 5)
                        self.powers.append(power(self.dino.get_position()))

        # Movement
        self.move_all_objects()

        # Enemies
        if (self.enemy.check_hitted(self.dino) and not self.enemy.get_hitted()):
            del self.enemy
            self.enemy = enemy(self.screen_size, self.ground_limit)
            self.dino.set_lives(1, type='decrement')
            if (not self.dino.get_lives()):
                return(True, 'game_over', None)

        # Prize
        self.check_prize_hitted()

        # Objects to show
        objects_to_show = {}
        objects_to_show['lives'] = self.dino.get_lives()
        objects_to_show['coins'] = self.dino.get_coins()
        objects_to_show['power'] = self.powers
        objects_to_show['char'] = self.dino
        objects_to_show['enemy'] = self.enemy
        objects_to_show['prize'] = self.prize
        self.clock.tick(self.difficulty * 60)
        return (True, 'match_running', objects_to_show)

    def check_prize_hitted(self):
        if (self.prize.hitted(self.dino.get_position(), self.dino.get_size())):
            if (self.prize.get_type()):
                self.dino.set_coins(self.prize.value(), type='increment')
            else:
                self.dino.set_lives(self.dino.get_lives() + 1)
            del self.prize
            self.prize = prize((self.screen_size[0], self.screen_size[1] - 170))

    def load_media(self):
        resources = {}
        numbers = {str(i): pygame.image.load('../resources/' + str(i) + '.png') for i in range(10)}
        resources['ground'] = pygame.image.load('../resources/ground.png')
        resources['numbers'] = numbers
        return resources

    def move_all_shots(self):
        """
            Takes all the shots, movement them and return a list with it.
        """
        moved = []
        for shot in self.powers:
            if shot.get_position()[0] > self.screen_size[0]:
                del shot
                continue
            if self.enemy.check_hitted(shot):
                del shot
                del self.enemy
                self.enemy = enemy(self.screen_size, self.ground_limit)
                continue
            shot.move()
            moved.append(shot)
        return moved

    def move_all_objects(self, velocity=5):
        # Dino
        self.dino.jump(self.ground_limit)
        # Powers
        self.powers = self.move_all_shots()
        # Enemies
        enemy_pos = self.enemy.get_position()
        if (not enemy_pos[0]):
            enemy_pos = (self.screen_size[0], enemy_pos[1])
        self.enemy.set_position((enemy_pos[0] - velocity, enemy_pos[1]))
        # Prizes
        prize_pos = self.prize.get_position()
        self.prize.set_position((prize_pos[0] - (velocity + 1), prize_pos[1]))
        if (self.prize.get_position()[0] <= 0):
            self.prize = prize((self.screen_size[0], self.screen_size[1] - 170))

    def get_dino(self):
        return self.dino
