import pygame
import os


def load_image(name):
    """Load an image and convert it to a Pygame surface at its original size."""
    image = pygame.image.load(os.path.join('res', name)).convert_alpha()
    return image
