import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
CHARACTER_SIZE = 50
CHARACTER_COLOR = (0, 128, 255)
GRAVITY = 1
JUMP_HEIGHT = -15

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumping Character")

# Character attributes
character_x = SCREEN_WIDTH // 4
character_y = SCREEN_HEIGHT - CHARACTER_SIZE
character_velocity_y = 0
jumping = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Jump when spacebar is pressed
    if keys[pygame.K_SPACE]:
        if not jumping:
            # Calculate the angle and distance to the mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - character_x
            dy = mouse_y - character_y
            distance = math.sqrt(dx**2 + dy**2)

            if distance > 0:
                # Calculate the jump velocity components
                jump_velocity = JUMP_HEIGHT / (distance / CHARACTER_SIZE)
                character_velocity_y = jump_velocity * (dy / distance)
                character_x_velocity = jump_velocity * (dx / distance)

                jumping = True

    if jumping:
        # Apply gravity
        #character_velocity_y += GRAVITY

        # Update character's position
        character_x += character_x_velocity
        character_y += character_velocity_y

        # Check if the character has reached the jump height
        if character_y >= SCREEN_HEIGHT - CHARACTER_SIZE:
            jumping = False
            character_y = SCREEN_HEIGHT - CHARACTER_SIZE
            character_velocity_y = 0

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the character
    pygame.draw.rect(screen, CHARACTER_COLOR, (character_x, character_y, CHARACTER_SIZE, CHARACTER_SIZE))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
