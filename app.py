import pygame
import random
import sys

"""
    MADE BY CutyCat#2329
    -- Do not steal my code --
"""

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

# Create the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Define the font and font size
font = pygame.font.SysFont(None, 20)

# Define the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define the characters to display
characters = ['0', '1']

# Define the speed range for each character
speed_range = [20, 60]

# Define the number of characters per 100x100 pixels
density = 3

# Define the delay between adding new characters
delay = 1

# Define a list to store the falling characters
falling_characters = []

# Define a function to add new falling characters
def add_characters():
    for i in range(density):
        x = random.randrange(0, screen_width)
        y = random.randrange(-100, 0)
        speed = random.randint(*speed_range)
        char = random.choice(characters)
        size = random.randint(10, 30)
        falling_characters.append({'x': x, 'y': y, 'speed': speed, 'char': char, 'size': size})

# Define a function to update the falling characters
def update_characters():
    for char in falling_characters:
        char['y'] += char['speed']
        if char['y'] > screen_height:
            falling_characters.remove(char)

# Define a function to draw the falling characters
def draw_characters():
    for char in falling_characters:
        text = font.render(char['char'], True, GREEN)
        text = pygame.transform.scale(text, (char['size'], char['size']))
        screen.blit(text, (char['x'], char['y']))

# Set the clock for the game loop
clock = pygame.time.Clock()

# Start the game loop
try:
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Update the falling characters
        update_characters()

        # Add new falling characters
        if random.randint(1, delay) == 1:
            add_characters()

        # Draw the falling characters
        draw_characters()

        # Update the screen
        pygame.display.update()

        # Set the game clock
        clock.tick(60)

except SystemExit:
    pygame.quit()
    sys.exit()
