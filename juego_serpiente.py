import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the Snake and Food
block_size = 10

class Snake:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.dx = 0
        self.dy = -block_size
        self.body = []
        self.length = 1
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # Check if snake goes out of bounds
        if self.x < 0 or self.x >= width or self.y < 0 or self.y >= height:
            return False
        
        # Check if snake collides with itself
        for block in self.body:
            if block[0] == self.x and block[1] == self.y:
                return False
        
        # Add new head to the body
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop(0)
        
        return True
    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(win, black, (block[0], block[1], block_size, block_size))
        
class Food:
    def __init__(self):
        self.x = random.randrange(0, width - block_size, block_size)
        self.y = random.randrange(0, height - block_size, block_size)
    
    def draw(self):
        pygame.draw.rect(win, red, (self.x, self.y, block_size, block_size))

# Set up the game loop
clock = pygame.time.Clock()
snake = Snake()
food = Food()
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -block_size
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = block_size
            elif event.key == pygame.K_LEFT:
                snake.dx = -block_size
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = block_size
                snake.dy = 0
    
    # Move the Snake and check for collisions
    if not snake.move():
        game_over = True
    elif snake.x == food.x and snake.y == food.y:
        snake.length += 1
        food = Food()
    
    # Draw the Snake and Food
    win.fill(white)
    snake.draw()
    food.draw()
    pygame.display.update()
    
    # Tick the clock
    clock.tick(10)

# Quit Pygame
pygame.quit()
