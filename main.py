import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BULLET_SPEED = 20
FPS = 60
SCORE = 0

self_size = (800, 600)
background_image = pygame.image.load("back_ground.jpg")
background_image = pygame.transform.scale(background_image, self_size)
background_rect = background_image.get_rect()

tower_image = pygame.image.load("Bplaceholder.png")
tower_image = pygame.transform.scale(tower_image, (50, 50))
tower_rect = tower_image.get_rect()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player properties
player_width = 50
player_height = 50
player_speed = 5
scroll_x = -2

PFont = pygame.font.Font('papyrus.ttf', 30)


def create_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (100, 100))


def create_bullet(x, y):
    return pygame.Rect(x, y, 10, 5)


def create_obstacle(x, y):
    return pygame.Rect(x, y, 50, 50)


obstacles = []
bullets = []

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("gaming window")

# Create the player object
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT // 2 - player_height // 2, player_width, player_height)

clock = pygame.time.Clock()  # Set up the clock
pygame.mouse.set_visible(0)  # Remove Cursor visability

# Set up the scoreboard, timer and difficulty increase


# ticks = pygame.time.get_ticks()
# seconds = ticks/10000000
# print(ticks)


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(create_bullet(player.x + 50, player.y + 50))



    # ticks = pygame.time.get_ticks()
    # seconds = ticks%10000000
    # print(seconds)

    scroll_x -= 3.5  # Adjust the scrolling speed as needed

    # CREATE ZE OBSTACLES
    #     if random.randint(0, 100) < 10:
    #         obstacles.append(create_obstacle(scroll_x, 300))

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

    if scroll_x <= -background_rect.width:  # Reset the scroll position when the image goes off-screen
        scroll_x = 0

    keys = pygame.key.get_pressed()  # Get the state of all keys

    # Update player position based on key presses
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    for bullet in bullets:
        bullet.x += BULLET_SPEED
        pygame.draw.rect(screen, RED, bullet)

    # Draw the player
    pygame.draw.rect(screen, RED, player)

    # DRAW ZE OBSTACLE
    # for obstacles in obstacles:
    #     screen.blit(tower_image, (scroll_x, 0))

    pygame.display.flip()  # Update the display

    clock.tick(FPS)  # Cap the frame rate

    create_text("FUCK!", PFont, (0, 0, 0), 100,100)