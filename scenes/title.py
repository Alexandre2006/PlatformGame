# Title Scene
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)
import pygame
import globals

from utils.scene import SceneBase

class TitleScene(SceneBase):
    def __init__(self):
        self.title_font = pygame.font.Font("./shared/fonts/Pixeboy.ttf", 32)

    def update(self, dt):
        self.dt = dt
        pass

    def render(self):
        # Clear screen
        globals.screen.fill((255, 255, 255))

        # Draw title
        title = self.title_font.render("ASCENT", True, (0, 0, 0))
        globals.screen.blit(title, ((globals.SCREEN_WIDTH - self.title_font.size("ASCENT")[0]) / 2, 0))

    def handle_events(self, events):
        pass # Title scene does not handle any events