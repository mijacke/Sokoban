import pygame
from assets import load_image


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.image = load_image('Ground_Dirt.png')  # Ensure you have this image
        self.rect = self.image.get_rect(topleft=(x, y))


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.image = load_image('Crate_Beige.png')  # Ensure you have this image
        self.rect = self.image.get_rect(topleft=(x, y))
