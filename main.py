# File written by Copilot

import pygame
from pygame.locals import *
from sys import exit
import globals

from utils.scene_manager import SceneManager

# Initialize globals
globals.init()

# Initialize pygame
pygame.init()

# Create game window
screen_width = 800
screen_height = 600
globals.screen = pygame.display.set_mode((screen_width, screen_height))

# Set window caption
pygame.display.set_caption("Platform Game")

# Create scene manager
scene_manager = SceneManager()

# Create scenes (TODO)

# Register scenes (TODO)

# Switch to the first scene (TODO)

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

    # Update screen
    pygame.display.flip()

