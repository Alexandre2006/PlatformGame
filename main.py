# File written by Copilot

import pygame
from pygame.locals import *
from sys import exit
import globals

from utils.scene_manager import SceneManager
from scenes.title import TitleScene

# Initialize globals
globals.init()

# Initialize pygame
pygame.init()

# Create game window
globals.SCREEN_WIDTH = 800
globals.SCREEN_HEIGHT = 600
globals.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

# Create clock
clock = pygame.time.Clock()

# Set window caption
pygame.display.set_caption("ASCENT (ATCS PlatformGame)")

# Create scene manager
scene_manager = SceneManager()

# Register scenes
scene_manager.register_scene("title", TitleScene())

# Switch to the first scene
scene_manager.switch_scene("title")

# Game loop
while True:
    # Get all events
    events = pygame.event.get()

    # Handle Quit event
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Update current scene
    scene_manager.update_current_scene()

    # Render current scene 
    scene_manager.render_current_scene()

    # Wait for next frame
    clock.tick(60)

    # Update screen
    pygame.display.flip()