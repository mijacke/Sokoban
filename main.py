import pygame
import os

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64
PLAYER_SPEED = 2.5  # Character speed

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Load game assets
def load_image(name):
    """Load an image and convert it to a Pygame surface."""
    image = pygame.image.load(os.path.join('res', name)).convert_alpha()
    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
    return image


# Player animation frames
player_frames = {
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
# Stationary frames when the player is not moving
stationary_frames = {
    'down': load_image('Character4.png'),
    'up': load_image('Character7.png'),
    'left': load_image('Character1.png'),
    'right': load_image('Character2.png'),
}

# Initial player position
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

# Current frame of the player's animation
current_frame = 0

# Player's direction
player_direction = 'down'

# Load wall image
wall_image = load_image('Wall_Brown.png')

# Timing for frame updates
frame_rate = 5
last_update = pygame.time.get_ticks()
frame_update_time = 1000 // frame_rate  # Update every 1000/frame_rate milliseconds

# The game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement keys
    keys = pygame.key.get_pressed()
    moving = False  # Track whether the player is moving
    new_direction = player_direction  # Track if the direction has changed

    if keys[pygame.K_a]:
        player_pos[0] -= PLAYER_SPEED
        new_direction = 'left'
        moving = True
    elif keys[pygame.K_d]:
        player_pos[0] += PLAYER_SPEED
        new_direction = 'right'
        moving = True
    elif keys[pygame.K_w]:
        player_pos[1] -= PLAYER_SPEED
        new_direction = 'up'
        moving = True
    elif keys[pygame.K_s]:
        player_pos[1] += PLAYER_SPEED
        new_direction = 'down'
        moving = True

    # If the direction has changed, reset the frame
    if new_direction != player_direction:
        player_direction = new_direction
        current_frame = 0  # Reset to the first frame of the new direction

    # Only update the animation frame at the specified interval
    current_time = pygame.time.get_ticks()
    if moving and current_time - last_update > frame_update_time:
        last_update = current_time
        current_frame = (current_frame + 1) % len(player_frames[player_direction])

    if moving:
        player_image = player_frames[player_direction][current_frame]
    else:
        current_frame = 0  # Reset to the first frame
        player_image = stationary_frames[player_direction]  # Use the stationary sprite

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen with black

    # Draw the walls, boxes, and player
    screen.blit(wall_image, (100, 100))
    screen.blit(player_image, player_pos)  # Draw the player at the new position

    # Update the display
    pygame.display.flip()

    # Frame rate control
    pygame.time.Clock().tick(60)  # You can adjust this for smoother or less smooth movement

pygame.quit()

