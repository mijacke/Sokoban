import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from level import Level


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    level = Level(SCREEN_WIDTH, SCREEN_HEIGHT)  # Create a Level instance

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update level and player
        level.update(keys)  # Pass the keys to level.update()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the level
        level.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
