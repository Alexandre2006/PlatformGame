import pygame

from utils.scene import SceneBase

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def update(self, dt):
        pass

    def render(self, dt):
        # Clear screen
        screen.fill((0, 0, 0))

        

    def handle_events(self, events):
        pass # Title scene does not handle any events