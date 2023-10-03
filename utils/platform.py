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
    IMAGE_GRASS = pygame.image.load("./shared/tiles/grass.png")
    IMAGE_ICE = pygame.image.load("./shared/tiles/ice.png")
    IMAGE_BOOST = pygame.image.load("./shared/tiles/boost.png")
    IMAGE_SPIKE = pygame.image.load("./shared/tiles/spike.png")

    # Platform Widths
    WIDTH_THIN = 1
    WIDTH_NORMAL = 2
    WIDTH_THICK = 3
    WIDTH_FLOOR = 10

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
    
    def getPlatformImage(self):
        if self.type == Platform.TYPE_GRASS:
            return Platform.IMAGE_GRASS
        elif self.type == Platform.TYPE_ICE:
            return Platform.IMAGE_ICE
        elif self.type == Platform.TYPE_BOOST:
            return Platform.IMAGE_BOOST
        elif self.type == Platform.TYPE_SPIKE:
            return Platform.IMAGE_SPIKE
    


platform_templates = [
    # Template 1 (Left side)
    [Platform(100, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(180, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(260, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 2 (Right side)
    [Platform(600, 0, Platform.TYPE_GRASS, Platform.WIDTH_THIN, 0), Platform(520, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(440, 0, Platform.TYPE_GRASS, Platform.WIDTH_THIN, 0)],
    
    # Template 3 (Left side)
    [Platform(50, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(130, 0, Platform.TYPE_SPIKE, Platform.WIDTH_NORMAL, 0), Platform(210, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 4 (Right side)
    [Platform(660, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(580, 0, Platform.TYPE_ICE, Platform.WIDTH_THIN, 0), Platform(500, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 5 (Left side)
    [Platform(20, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(100, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(180, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 6 (Moving platform - Left side)
    [Platform(50, 0, Platform.TYPE_GRASS, Platform.WIDTH_THICK, 2)],
    
    # Template 7 (Moving platform - Right side)
    [Platform(660, 0, Platform.TYPE_GRASS, Platform.WIDTH_THICK, -2)],
    
    # Template 8 (Left side)
    [Platform(20, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(100, 0, Platform.TYPE_BOOST, Platform.WIDTH_THICK, 0), Platform(180, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 9 (Right side)
    [Platform(660, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(580, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(500, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 10 (Left side)
    [Platform(50, 0, Platform.TYPE_SPIKE, Platform.WIDTH_NORMAL, 0), Platform(130, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(210, 0, Platform.TYPE_SPIKE, Platform.WIDTH_NORMAL, 0)],
    
    # Template 11 (Right side)
    [Platform(600, 0, Platform.TYPE_GRASS, Platform.WIDTH_THIN, 0), Platform(520, 0, Platform.TYPE_BOOST, Platform.WIDTH_THICK, 0)],
    
    # Template 12 (Left side)
    [Platform(100, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(180, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(260, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 13 (Right side)
    [Platform(600, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(520, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(440, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 14 (Left side)
    [Platform(20, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(100, 0, Platform.TYPE_SPIKE, Platform.WIDTH_NORMAL, 0), Platform(180, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 15 (Right side)
    [Platform(660, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(580, 0, Platform.TYPE_GRASS, Platform.WIDTH_THIN, 0), Platform(500, 0, Platform.TYPE_GRASS, Platform.WIDTH_THICK, 0)],
    
    # Template 16 (Left side)
    [Platform(50, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(130, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(210, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 17 (Right side)
    [Platform(660, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(580, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(500, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 18 (Left side)
    [Platform(100, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(180, 0, Platform.TYPE_BOOST, Platform.WIDTH_NORMAL, 0), Platform(260, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 19 (Right side)
    [Platform(600, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(520, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(440, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0)],
    
    # Template 20 (Left side)
    [Platform(20, 0, Platform.TYPE_GRASS, Platform.WIDTH_THICK, 0), Platform(100, 0, Platform.TYPE_GRASS, Platform.WIDTH_NORMAL, 0), Platform(180, 0, Platform.TYPE_GRASS, Platform.WIDTH_THICK, 0)],
]