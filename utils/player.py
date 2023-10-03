# Player Class
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)

import pygame
import globals
from utils.platform import Platform

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
    
    def checkPlatformPerfectCollision(self, platforms):
        # Perfect collision triggers effects, and when y of player is same as y of platform
        for i in platforms:
            if self.y - Player.CHARACTER_HEIGHT == i.y and self.x <= i.x + i.width and self.x + Player.CHARACTER_WIDTH >= i.x:
                return i

    def checkPlatformCollision(self, prev_x, prev_y, platforms):
        # Check for collision with platforms (going down)
        for i in platforms:
            if prev_y >= i.y and self.y <= i.y and self.x <= i.x + i.width and self.x + Player.CHARACTER_WIDTH >= i.x:
                self.y = i.y
                self.y_velocity = 0
                return True
        
        # Check for collision with platforms (going up)
        for i in platforms:
            if prev_y < i.y and self.y >= i.y and self.x <= i.x + i.width and self.x + Player.CHARACTER_WIDTH >= i.x:
                self.y = i.y + 160
                self.y_velocity = 0
                return True
        
        # Check for collision with platforms (going right)
        for i in platforms:
            if prev_x < i.x and self.x >= i.x and self.y <= i.y + 80 and self.y + Player.CHARACTER_HEIGHT >= i.y:
                self.x = i.x + i.width
                self.x_velocity = 0
                return True

        # Check for collision with platforms (going left)
        for i in platforms:
            if prev_x > i.x and self.x <= i.x and self.y <= i.y + 80 and self.y + Player.CHARACTER_HEIGHT >= i.y:
                self.x = i.x - Player.CHARACTER_WIDTH
                self.x_velocity = 0
                return True


    def update(self, dt, platforms):
        prev_x = self.x
        prev_y = self.y

        # Check for collisions with platforms
        perfect_collision = self.checkPlatformPerfectCollision(platforms)
        if perfect_collision != None:
            if perfect_collision.type == Platform.TYPE_BOOST:
                self.y_velocity = 20
            elif perfect_collision.type == Platform.TYPE_SPIKE:
                globals.scene_manager.switch_scene("title")
            elif perfect_collision.type == Platform.TYPE_ICE:
                self.x_velocity *= 0.95
                self.y_velocity = 0
            else:
                self.x_velocity = 0.8
                self.y_velocity = 0

        # Update position based on velocity
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt

        # Check for other collisions
        self.checkPlatformCollision(prev_x, prev_y, platforms)

        # Check for all types of collisions
        self.checkWallCollision()

        # Update gravity
        self.y_velocity -= 0.5 * dt
