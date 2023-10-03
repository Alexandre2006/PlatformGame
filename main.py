# Main File
# Entirely written by humans, with assistance from Copilot (75% human, 25% AI)

import pygame
from pygame.locals import *
from sys import exit
import globals
from scenes.death import DeathScene

from utils.scene_manager import SceneManager
from scenes.title import TitleScene

# Initialize globals
globals.init()

# Initialize pygame
pygame.init()

# Create game window
globals.SCREEN_WIDTH = 800
globals.SCREEN_HEIGHT = 800
globals.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

# Create clock
clock = pygame.time.Clock()

# Init Music
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

# Set window caption
pygame.display.set_caption("ASCENT (ATCS PlatformGame)")

# Create scene manager
globals.scene_manager = SceneManager()

# Register scenes
globals.scene_manager.register_scene("title", TitleScene())

# Switch to the first scene
globals.scene_manager.switch_scene("title")

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
    globals.scene_manager.update_current_scene()

    # Render current scene 
    globals.scene_manager.render_current_scene()

    # Wait for next frame
    clock.tick(60)

    # Update screen
    pygame.display.flip()