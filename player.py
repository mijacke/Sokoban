import pygame
from assets import load_image
from settings import FRAME_RATE


class Player(pygame.sprite.Sprite):
    def __init__(self, tile_size, start_pos):
        super().__init__()
        self.frames = {
            'down': [load_image('Character4.png'), load_image('Character5.png'), load_image('Character6.png')],
            'up': [load_image('Character7.png'), load_image('Character8.png'), load_image('Character9.png')],
            'left': [load_image('Character1.png'), load_image('Character10.png')],
            'right': [load_image('Character2.png'), load_image('Character3.png')],
        }
        self.stationary_frames = {
            'down': load_image('Character4.png'),
            'up': load_image('Character7.png'),
            'left': load_image('Character1.png'),
            'right': load_image('Character2.png'),
        }
        self.direction = 'down'
        self.image = self.stationary_frames[self.direction]
        self.rect = self.image.get_rect(topleft=start_pos)
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_update_time = 1000 // FRAME_RATE
        self.tile_size = tile_size
        self.move_cooldown = 500  # Adjust if needed for smoother movement
        self.last_move = 0

    def update(self, keys, layout):
        current_time = pygame.time.get_ticks()
        x_change = y_change = 0  # Initialize x_change and y_change at the start

        if current_time - self.last_move > self.move_cooldown:
            if keys[pygame.K_a]:
                x_change = -self.tile_size
            if keys[pygame.K_d]:
                x_change = self.tile_size
            if keys[pygame.K_w]:
                y_change = -self.tile_size
            if keys[pygame.K_s]:
                y_change = self.tile_size

            next_x, next_y = self.rect.x + x_change, self.rect.y + y_change
            grid_x, grid_y = next_x // self.tile_size, next_y // self.tile_size

            if len(layout[0]) > grid_x >= 0 == layout[grid_y][grid_x] and 0 <= grid_y < len(layout):
                self.rect.x, self.rect.y = next_x, next_y
                self.last_move = current_time
                self.direction = 'left' if x_change < 0 else 'right' if x_change > 0 else 'up' if y_change < 0 else 'down' if y_change > 0 else self.direction

        # Animation
        if current_time - self.last_update > self.frame_update_time:
            self.current_frame = (self.current_frame + 1) % len(self.frames[self.direction])
            self.image = self.frames[self.direction][self.current_frame]
            self.last_update = current_time
        if not (x_change or y_change):  # This check is now safe with x_change and y_change initialized
            self.image = self.stationary_frames[self.direction]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
