# Main Game Scene
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)
import pygame
import globals
from utils.camera import Camera
from utils.player import Player

from utils.scene import SceneBase


class GameScene(SceneBase):
    def __init__(self):
        self.camera = Camera()
        self.player = Player()

    def update(self, dt):
        pass

    def render(self):
        # Clear screen
        globals.screen.fill((255, 255, 255))

        # Render player
        globals.screen.blit(self.player.IMAGE, (self.player.x, self.camera.calculate_pygame_pos(self.player.y)))

    def handle_events(self, events):
        pass