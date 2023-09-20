#Untested

import pygame

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 9.81

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the player sprite
player = pygame.image.load("player.png")

# Create a sprite group for the player
player_group = pygame.sprite.Group()
player_group.add(player)

# Create a sprite group for the platforms
platform_group = pygame.sprite.Group()

# Create the first platform
platform = pygame.sprite.Sprite()
platform.image = pygame.Surface((100, 20))
platform.image.fill((0, 255, 0))
platform.rect = platform.image.get_rect()
platform.rect.x = 100
platform.rect.y = 300
platform_group.add(platform)

# Create the game clock
clock = pygame.time.Clock()

# Game loop
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the player's position
    player.rect.y += GRAVITY
    if player.rect.colliderect(platform.rect):
        player.rect.y = platform.rect.top - player.rect.height

    # Check for collisions with platforms
    for platform in platform_group:
        if player.rect.colliderect(platform.rect):
            player.rect.y = platform.rect.top - player.rect.height

    # Draw the game window
    screen.fill((0, 0, 0))
    player_group.draw(screen)
    platform_group.draw(screen)
    pygame.display.flip()

    # Limit the framerate
    clock.tick(60)
