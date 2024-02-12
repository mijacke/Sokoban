import pygame
from assets import load_image
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED, FRAME_RATE


class Player(pygame.sprite.Sprite):
    def __init__(self, tile_size, start_pos):
        super().__init__()
        self.frames = {
            'down': [load_image('Character4.png'),
                     load_image('Character5.png'),
                     load_image('Character6.png')],
            'up': [load_image('Character7.png'),
                   load_image('Character8.png'),
                   load_image('Character9.png')],
            'left': [load_image('Character1.png'),
                     load_image('Character10.png')],
            'right': [load_image('Character2.png'),
                      load_image('Character3.png')],
        }
        self.stationary_frames = {
            'down': load_image('Character4.png'),
            'up': load_image('Character7.png'),
            'left': load_image('Character1.png'),
            'right': load_image('Character2.png'),
        }
        self.image = self.stationary_frames['down']
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.direction = 'down'
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_update_time = 1000 // FRAME_RATE
        self.move_cooldown = 500  # 500 milliseconds cooldown
        self.last_move = pygame.time.get_ticks()
        self.tile_size = tile_size
        self.rect.topleft = start_pos  # Position based on grid start position

    def update(self, keys, layout):
        moving = False
        x_change = 0
        y_change = 0

        if keys[pygame.K_a]:
            x_change = -self.tile_size
            new_direction = 'left'
        elif keys[pygame.K_d]:
            x_change = self.tile_size
            new_direction = 'right'
        elif keys[pygame.K_w]:
            y_change = -self.tile_size
            new_direction = 'up'
        elif keys[pygame.K_s]:
            y_change = self.tile_size
            new_direction = 'down'

        # Example collision check (simplified)
        # Next position on grid
        next_x = self.rect.x + x_change
        next_y = self.rect.y + y_change

        # Convert next_x and next_y to grid coordinates
        grid_x = next_x // self.tile_size
        grid_y = next_y // self.tile_size

        current_time = pygame.time.get_ticks()
        if current_time - self.last_move > self.move_cooldown:
            if 0 <= grid_x < len(layout[0]) and 0 <= grid_y < len(layout):
                if layout[grid_y][grid_x] == 0:  # Assuming '0' represents an empty space
                    moving = True
                    self.rect.x = next_x
                    self.rect.y = next_y
                    self.last_move = current_time

        # Update direction and animation frame
        new_direction = self.direction  # Add this line at the start of the update method
        if moving:
            if new_direction != self.direction:
                self.direction = new_direction
                self.current_frame = 0
            self.image = self.frames[self.direction][self.current_frame]
            self.last_update = pygame.time.get_ticks()  # Reset the timer
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update > self.frame_update_time:
                self.last_update = current_time
                self.last_move = current_time
                self.current_frame = (self.current_frame + 1) % len(self.frames[self.direction])
                self.image = self.frames[self.direction][self.current_frame]
        else:
            self.current_frame = 0
            self.image = self.stationary_frames[self.direction]

    def draw(self, screen):
        screen.blit(self.image, self.rect)