# Main Game Scene
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)
import math
import random
import pygame
import globals
from utils.camera import Camera
from utils.platform import Platform
from utils.platform_gen import PlatformGenerator
from utils.player import Player

from utils.scene import SceneBase


class GameScene(SceneBase):
    def __init__(self):
        self.camera = Camera()
        self.player = Player()
        self.angle = 0
        self.platforms = [
            Platform(0, 100, Platform.TYPE_GRASS, platform_width_type=Platform.WIDTH_FLOOR, platform_x_velocity=0),
            Platform(0, 400, Platform.TYPE_GRASS, platform_width_type=Platform.WIDTH_THICK, platform_x_velocity=0),
            Platform(560, 400, Platform.TYPE_GRASS, platform_width_type=Platform.WIDTH_THICK, platform_x_velocity=0),
            Platform(280, 700, Platform.TYPE_GRASS, platform_width_type=Platform.WIDTH_THICK, platform_x_velocity=0),
            Platform(0, 1000, Platform.TYPE_ICE, platform_width_type=Platform.WIDTH_THICK, platform_x_velocity=0),
            Platform(280, 1000, Platform.TYPE_SPIKE, platform_width_type=Platform.WIDTH_THIN, platform_x_velocity=0),
            Platform(560, 1000, Platform.TYPE_ICE, platform_width_type=Platform.WIDTH_THICK, platform_x_velocity=0),
            ]

    def update(self, dt):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_x, player_y = self.player.x + (Player.CHARACTER_WIDTH / 2), self.camera.calculate_pygame_pos(self.player.y)

        # This line is entirely generated by Copilot
        self.angle = math.atan2(mouse_y - player_y, mouse_x - player_x)

        # Process Jump
        if pygame.mouse.get_pressed()[0] and self.player.checkCanJump(self.platforms):

            self.player.jump(self.angle)
        
        # Update player
        self.player.update(dt, self.platforms)

        # Update Camera
        self.camera.move_to(self.player.y - (Player.CHARACTER_HEIGHT + globals.SCREEN_HEIGHT / 2))

        # Remove any platforms that are off screen from list
        heights_removed = []
        for i in self.platforms:
            print(i.y, self.camera.y)
            if i.y < self.camera.y:
                if i.y not in heights_removed:
                    heights_removed.append(i.y)
                self.platforms.remove(i)
        
        # Randomly add platforms from platform_templates (list of list of templates), for each height removed. first height is 300 above highest height remaining, second height is 300 above that, etc.
        greatest_height = 0
        for i in self.platforms:
            if i.y > greatest_height:
                greatest_height = i.y
    
        for i in range(0, len(heights_removed)):
            plat_template = PlatformGenerator.getPlatforms()
            for j in plat_template:
                j.y = greatest_height + ((i+1) * 300)
                self.platforms.append(j)
        
        # Update platforms
        for i in self.platforms:
            i.update(dt)
        
        # Check if player is dead
        if self.player.y < self.camera.y:
            globals.scene_manager.switch_scene("title")

    def render(self):
        # Clear screen
        globals.screen.fill((255, 255, 255))

        # Render player
        globals.screen.blit(self.player.IMAGE, (self.player.x, self.camera.calculate_pygame_pos(self.player.y)))

        # Render arrow (THIS LINE IS FULLY GENERATED BY COPILOT)
        pygame.draw.line(globals.screen, (0, 0, 0), (self.player.x + (Player.CHARACTER_WIDTH / 2), self.camera.calculate_pygame_pos(self.player.y)), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 5)
        # Render platforms (platform image repeats every 80 pixels)
        for i in self.platforms:
            for j in range(0, i.width, 80):
                globals.screen.blit(i.getPlatformImage(), (i.x + j, self.camera.calculate_pygame_pos(i.y)))

    def handle_events(self, events):
        pass