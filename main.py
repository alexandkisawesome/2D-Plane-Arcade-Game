import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BULLET_SPEED = 20
FPS = 60
SCORE = 0
gameTicks = 0
PFont = pygame.font.Font("papyrus.ttf",20)


self_size = (800,600)
win = pygame.display.set_mode((800,600))
background_image = pygame.image.load("back_ground.jpg")
background_image = pygame.transform.scale(background_image, self_size)
background_rect = background_image.get_rect()


#tower_image = pygame.image.load("Bplaceholder.png")
#tower_image = pygame.transform.scale(tower_image, (50, 50))
#tower_rect = tower_image.get_rect()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
scroll_x = -1


class enemyTower():

    def __init__(self):
        self.speed = 12
        self.y = 0
        self.x = 600
        self.x = scroll_x
        self.image = pygame.image.load("tower1.png")
        self.size = (70, 175)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.frequency = 25

class BirdEnemy:
    def __init__(self):
        self.speed = 3
        self.size = (50, 50)
        self.image = pygame.image.load("bird.png")  # Replace with your bird image file
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH  # Start off-screen
        self.rect.y = random.randint(0, HEIGHT - self.size[1])  # Random vertical position

    def move_towards_player(self, player):
        if self.rect.x > player.x:
            self.rect.x -= self.speed
        elif self.rect.x < player.x:
            self.rect.x += self.speed

        if self.rect.y > player.y:
            self.rect.y -= self.speed
        elif self.rect.y < player.y:
            self.rect.y += self.speed
            
class player():
    def __init__(self):
        self.x = 200
        self.y = 200
        self.speed = 5
        self.size = (100, 100)
        self.image = pygame.image.load("plane.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)

    def moveLeft(self):
        self.x = self.x - self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])

    def moveRight(self):
        self.x = self.x + self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])

    def moveUp(self):
        self.y = self.y - self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])

    def moveDown(self):
        self.y = self.y + self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])


p1 = player()
enemy = enemyTower()

def towerfunction():
    if enemy.x<0:
        enemy.x=601
    win.blit(enemy.image, (enemy.x,enemy.y))
    return

def create_bullet(x, y):
    return pygame.Rect(x, y, 10, 5)


def create_obstacle(x, y):
    return pygame.Rect(x, y, 50, 50)


obstacles = []
bullets = []
birds = []

#enemytower = enemyTower()
# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("win")


# Set up the clock
clock = pygame.time.Clock()

# Game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(create_bullet(p1.x+75, p1.y+45))
    scroll_x -= 5
    # Adjust the scrolling speed as needed


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
    if keys[pygame.K_UP]:
        p1.moveUp()
    if keys[pygame.K_DOWN]:
        p1.moveDown()
    if keys[pygame.K_LEFT]:
        p1.moveLeft()
    if keys[pygame.K_RIGHT]:
        p1.moveRight()

    for bullet in bullets:
        bullet.x += BULLET_SPEED
        pygame.draw.rect(screen, RED, bullet)

    # Draw the player
    win.blit(p1.image, p1.rect)

    # Update the display
    pygame.display.flip()

    clock.tick(FPS)  # Cap the frame rate

    pygame.mouse.set_visible(False)

    # time = pygame.time.get_ticks()


    gameTicks += 1

    if gameTicks % 200 == 0:
        scroll_x -= 1

    print("score:",scroll_x)
    print(gameTicks)