import pygame
import globals
from utils.camera import Camera

from utils.scene import SceneBase


class GameScene(SceneBase):
    def __init__(self):
        self.camera = Camera()

    def update(self, dt):
        pass

    def render(self):
        # Clear screen
        globals.screen.fill((255, 255, 255))

    def handle_events(self, events):
        pass