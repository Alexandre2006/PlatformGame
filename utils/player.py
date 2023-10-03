# Player Class
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)

import pygame
import globals

class Player:
    CHARACTER_WIDTH = 80
    CHARACTER_HEIGHT = 160
    IMAGE = pygame.transform.scale(pygame.image.load("./shared/player/player.png"), (80, 160))

    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_velocity = 0
        self.y_velocity = 0
    
    def checkWallCollision(self):
        # Check for collision with right side of the screen
        if (self.x + Player.CHARACTER_WIDTH) > globals.SCREEN_WIDTH:
            self.x = globals.SCREEN_WIDTH - Player.CHARACTER_WIDTH
        
        # Check for collision with left side of the screen
        if self.x < 0:
            self.x = 0
    
    def update(self, dt):
        # Update position based on velocity
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt

        # Update gravity
        self.y_velocity -= globals.GRAVITY * dt

        # Check for all types of collisions
        self.checkWallCollision()
