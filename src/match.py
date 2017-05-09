import pygame
from enemy import enemy
from coin import coin


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
        self.coin = coin((self.screen_size[0], self.screen_size[1] - 170))
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

        # Movement
        self.move_all_objects()

        # Enemies
        if (self.enemy.check_hitted(self.dino) and not self.enemy.get_hitted()):
            del self.enemy
            self.enemy = enemy(self.screen_size, self.ground_limit)
            self.dino.set_lives(1, type='decrement')
            if (not self.dino.get_lives()):
                self.dino.reset()
                return(True, 'game_over', None)

        # Coins
        self.check_coin_hitted()

        # Objects to show
        objects_to_show = {}
        objects_to_show['lives'] = self.dino.get_lives()
        objects_to_show['coins'] = self.dino.get_coins()
        objects_to_show['char'] = self.dino
        objects_to_show['enemy'] = self.enemy
        objects_to_show['coin'] = self.coin
        self.clock.tick(self.difficulty * 60)
        return (True, 'match_running', objects_to_show)

    def check_coin_hitted(self):
        if (self.coin.hitted(self.dino.get_position(), self.dino.get_size())):
            self.dino.set_coins(self.coin.value(), type='increment')
            del self.coin
            self.coin = coin((self.screen_size[0], self.screen_size[1] - 170))

    def load_media(self):
        resources = {}
        numbers = {str(i): pygame.image.load('../resources/' + str(i) + '.png') for i in range(10)}
        resources['ground'] = pygame.image.load('../resources/ground.png')
        resources['numbers'] = numbers
        return resources

    def move_all_objects(self, velocity=5):
        # Dino
        self.dino.jump(self.ground_limit)
        # Enemies
        enemy_pos = self.enemy.get_position()
        if (not enemy_pos[0]):
            enemy_pos = (self.screen_size[0], enemy_pos[1])
        self.enemy.set_position((enemy_pos[0] - velocity, enemy_pos[1]))
        # Coins
        coin_pos = self.coin.get_position()
        self.coin.set_position((coin_pos[0] - velocity, coin_pos[1]))
        if (self.coin.get_position()[0] <= 0):
            self.coin = coin((self.screen_size[0], self.screen_size[1] - 170))
