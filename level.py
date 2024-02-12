import pygame

from player import Player
from game_objects import Wall


class Level:
    def __init__(self, screen_width, screen_height):
        self.tile_size = 64
        self.layout = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 'P', 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.player = Player(self.tile_size, self.get_player_start_position())
        self.walls = self.create_walls()

    def get_player_start_position(self):
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == 'P':
                    return x * self.tile_size, y * self.tile_size

    def create_walls(self):
        walls = pygame.sprite.Group()
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == 1:
                    wall = Wall(x * self.tile_size, y * self.tile_size, self.tile_size)
                    walls.add(wall)
        return walls

    def update(self, keys):
        self.player.update(keys, self.layout)

    def draw(self, screen):
        self.walls.draw(screen)
        self.player.draw(screen)
