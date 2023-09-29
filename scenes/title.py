import pygame
import globals

from utils.scene import SceneBase


class TitleScene(SceneBase):
    def __init__(self):
        self.title_font = pygame.font.Font("./shared/fonts/WayfarersFont.ttf", 32)
        self.background_image = pygame.image.load("./shared/backgrounds/title_screen.png")
        SceneBase.__init__(self)

    def update(self, dt):
        self.dt = dt
        pass

    def render(self):
        # Clear screen
        globals.screen.fill((255, 255, 255))

        # Set background image (fill screen, using pygame.transform.scale)
        globals.screen.blit(pygame.transform.scale(self.background_image, (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)), (0, 0))


        # Draw title on gray background rectangle (font size 72)
        title = self.title_font.render("Mountain Climb", True, (0, 0, 0))
        title_rect = title.get_rect()
        title_rect.center = (globals.SCREEN_WIDTH * (1/2) , globals.SCREEN_HEIGHT * (1/8))
        pygame.draw.rect(globals.screen, (200, 200, 200), title_rect.inflate(100, 100))
        globals.screen.blit(title, title_rect)

    def handle_events(self, events):
        pass # Title scene does not handle any events