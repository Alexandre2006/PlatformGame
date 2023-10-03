# Platform Class
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)

import pygame


class Platform:
    # Platform Types
    TYPE_GRASS = 0
    TYPE_ICE = 1
    TYPE_BOOST = 2
    TYPE_SPIKE = 3

    # Platform Images
    IMAGE_GRASS = pygame.image.load("./shared/platforms/grass.png")
    IMAGE_ICE = pygame.image.load("./shared/platforms/ice.png")
    IMAGE_BOOST = pygame.image.load("./shared/platforms/boost.png")
    IMAGE_SPIKE = pygame.image.load("./shared/platforms/spike.png")

    # Platform Widths
    WIDTH_THIN = 1
    WIDTH_NORMAL = 2
    WIDTH_THICK = 3

    # Platform Info
    width = 80
    x = 0
    y = 0
    x_velocity = 0
    type = TYPE_GRASS

    # Platform Stick Info
    move_player_by = 0

    # Constructor (x, y, type, width_type, velocity)
    def __init__(self, x_pos, y_pos, platform_type, platform_width_type, platform_x_velocity):
        self.x = x_pos
        self.y = y_pos
        self.type = platform_type
        self.width = platform_width_type * 80
        self.x_velocity = platform_x_velocity

    def update(self, dt):
        self.move_player_by = self.x_velocity * dt
        self.x += self.x_velocity * dt

        # Check if platform is off screen
        if self.x < 0:
            x = 0
            x_velocity *= -1
        
        if (self.x + self.width) > 800:
            self.x = 800 - self.width
            self.x_velocity *= -1
    

