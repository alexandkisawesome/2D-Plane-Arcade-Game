import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

self_size = (800, 600)
background_image = pygame.image.load("back_ground.jpg")
background_image = pygame.transform.scale(background_image, self_size)
background_rect = background_image.get_rect()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player properties
player_width = 50
player_height = 50
player_speed = 5
scroll_x = -2

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Up and Down Movement")

# Create the player object
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT // 2 - player_height // 2, player_width, player_height)

# Set up the clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    scroll_x -= 2

    # Adjust the scrolling speed as needed
    #     if random.randint(0, obstacle_spawn_rate) == 0:
    #         obstacle = pygame.Rect(WIDTH, random.randint(0, HEIGHT - obstacle_height), obstacle_width, obstacle_height)
    #         obstacles.append(obstacle)

    # Move obstacles
    # for obstacle in obstacles:
    #     obstacle.x -= obstacle_speed

    # Remove obstacles that go off-screen
    # obstacles = [obstacle for obstacle in obstacles if obstacle.x + obstacle.width > 0]
    #
    # for obstacle in obstacles:
    #     if player.colliderect(obstacle):
    #     print("Game Over!")  # Replace with your game over logic

    # Draw the background image twice to create a continuous scroll effect
    screen.blit(background_image, (scroll_x, 0))
    screen.blit(background_image, (scroll_x + background_rect.width, 0))

    # # Reset the scroll position when the image goes off-screen
    if scroll_x <= -background_rect.width:
        scroll_x = 0

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update player position based on key presses
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed

    # Draw the player
    pygame.draw.rect(screen, RED, player)
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
