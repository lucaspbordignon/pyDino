import pygame
from enemy import enemy
from coin import coin


class match():
    def __init__(self, surface, screen_settings, dino, difficulty=1):
        self.ground = {}
        # Frame
        self.clock = pygame.time.Clock()
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        # Media
        self.resources = self.load_media()
        # General
        ground_x = self.resources['ground'].get_width()
        ground_y = self.resources['ground'].get_height()
        self.ground['size'] = (ground_x, ground_y)
        self.ground['pos'] = (0, self.screen_size[1] - ground_y)
        self.ground['y_threshold'] = self.ground['pos'][1] + ground_y / 2
        self.dino = dino
        self.enemy = enemy(self.screen_size, self.ground)
        self.coin = coin((self.screen_size[0], self.screen_size[1] - 170))
        self.difficulty = difficulty

    def start(self):
        # Setup
        pygame.display.set_caption(self.caption + ': Playing')
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '')
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_UP and
                            not self.dino.is_jumping()):
                        self.dino.set_movement(8)
                        self.dino.set_jumping(True)
                    if (event.key == pygame.K_DOWN):
                        self.dino.set_movement(-5)

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], self.ground['pos'])

            # Movement
            self.move_all_objects()

            # Enemies
            if (self.enemy_hitted(self.dino, self.enemy) and not self.enemy.get_alreadyHit()):
                self.enemy.set_alreadyHit(True)
                self.dino.set_lives(self.dino.get_lives() - 1)
                if (self.dino.get_lives() == 0):
                    return(1, 'game_over')

            # Lives
            self.show_lives(self.dino)

            # Coins
            self.show_coins(self.dino)
            if (self.coin.hitted(self.dino.get_position(), self.dino.get_size())):
                self.dino.set_coins(1, type='increment')
                del self.coin
                self.coin = coin((self.screen_size[0], self.screen_size[1] - 170))

            # Updates the game display
            pygame.display.flip()
            self.clock.tick(60)

    def ground_threshold(self):
        ground_pos = self.ground['pos']
        ground_size = self.ground['size']
        dino_pos = self.dino.get_position()
        dino_size = self.dino.get_size()
        if (dino_pos[1] + dino_size[1] >= self.ground['y_threshold']):
            self.dino.set_movement(0)
            self.dino.set_jumping(False)
            dino_pos = (dino_pos[0], ground_pos[1] + (ground_size[1] / 2) - (dino_size[1] + 1))
        return dino_pos

    def enemy_hitted(self, dino, enemy):
        dino_pos = dino.get_position()
        dino_size = dino.get_size()
        enemy_pos = enemy.get_position()
        enemy_size = enemy.get_size()
        if (enemy_pos[0] <= dino_pos[0] + dino_size[0] <= enemy_pos[0] + enemy_size[0]):
            if (dino_pos[1] + dino_size[1] >= enemy_pos[1]):
                return True
        return False

    def load_media(self):
        resources = {}
        numbers = {str(i): pygame.image.load('../resources/' + str(i) + '.png') for i in range(10)}
        resources['ground'] = pygame.image.load('../resources/ground.png')
        resources['numbers'] = numbers
        return resources

    def show_lives(self, dino, pos=(40, 40)):
        lives = str(dino.get_lives())
        if (len(lives) < 2):
            images = (self.resources['numbers']['0'],
                      self.resources['numbers'][lives])
        else:
            images = (self.resources['numbers'][lives[0]],
                      self.resources['numbers'][lives[1]])
        position = (pos, (pos[0] + images[0].get_width(), pos[1]))

        self.screen.blit(images[0], position[0])
        self.screen.blit(images[1], position[1])

    def show_coins(self, dino, pos=(150, 40)):
        coins = str(dino.get_coins())
        if (len(coins) < 2):
            images = (self.resources['numbers']['0'],
                      self.resources['numbers'][coins])
        else:
            images = (self.resources['numbers'][coins[0]],
                      self.resources['numbers'][coins[1]])
        position = (pos, (pos[0] + images[0].get_width(), pos[1]))

        self.screen.blit(images[0], position[0])
        self.screen.blit(images[1], position[1])

    def move_all_objects(self, velocity=5):
        # Dino
        self.dino.jump(self.ground_threshold())
        # Enemies
        enemy_pos = self.enemy.get_position()
        if (not enemy_pos[0]):
            self.enemy.set_alreadyHit(False)
            enemy_pos = (self.screen_size[0], enemy_pos[1])
        self.enemy.set_position((enemy_pos[0] - velocity, enemy_pos[1]))
        # Ground
        self.ground['pos'] = (self.ground['pos'][0] - velocity, self.ground['pos'][1])
        if (self.ground['pos'][0] + self.ground['size'][0] == self.screen_size[0]):
            self.ground['pos'] = (0, self.ground['pos'][1])
        # Coins
        coin_pos = self.coin.get_position()
        self.coin.set_position((coin_pos[0] - velocity, coin_pos[1]))
        if (self.coin.get_position()[0] <= 0):
            self.coin = coin((self.screen_size[0], self.screen_size[1] - 170))

        self.screen.blit(self.enemy.get_image(), self.enemy.get_position())
        self.screen.blit(self.coin.get_image(), self.coin.get_position())
        self.screen.blit(self.dino.get_image(), self.dino.get_position())
