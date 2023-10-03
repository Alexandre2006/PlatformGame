# Title Scene
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)
import pygame
import globals
from scenes.game import GameScene

from utils.scene import SceneBase

class TitleScene(SceneBase):
    def __init__(self):
        self.title_font = pygame.font.Font("./shared/fonts/Pixeboy.ttf", 160)
        self.button_font = pygame.font.Font("./shared/fonts/Pixeboy.ttf", 40)
        self.mouse_pressed = False
        self.mouse_prev_pressed = False

    def update(self, dt):
        self.dt = dt
        self.mouse_prev_pressed = self.mouse_pressed
        self.mouse_pressed = pygame.mouse.get_pressed()[0]
        pass

    def render(self):
        # Clear screen
        globals.screen.fill((255, 255, 255))

        # Add background
        background = pygame.image.load("./shared/backgrounds/title.png")
        globals.screen.blit(background, (0, 0))

        # Draw title
        title = self.title_font.render("ASCENT", True, (0, 0, 0))
        globals.screen.blit(title, ((globals.SCREEN_WIDTH - self.title_font.size("ASCENT")[0]) / 2, 76))

        # Draw subtitle
        subtitle = self.button_font.render("A Platformer by Landon M. & Alexandre H.", True, (0, 0, 0))
        globals.screen.blit(subtitle, ((globals.SCREEN_WIDTH - self.button_font.size("A Platformer by Landon M. & Alexandre H.")[0]) / 2, 170))

        # Cursor Position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Add play button
        play_button_x = (globals.SCREEN_WIDTH - self.button_font.size("Start Game")[0]) / 2
        play_button_y = 350
        play_button_width = self.button_font.size("Start Game")[0] 
        play_button_height = self.button_font.size("Start Game")[1]

        play_box_x = play_button_x - 50
        play_box_y = play_button_y - (play_button_height / 2) - 20
        play_box_width = play_button_width + 100
        play_box_height = play_button_height + play_button_height + 40

        play_box_color = (128, 128, 128)

        if mouse_x > play_box_x and mouse_x < play_box_x + play_box_width and mouse_y > play_box_y and mouse_y < play_box_y + play_box_height:
            play_box_color = (196, 196, 196)
            if self.mouse_prev_pressed and not self.mouse_pressed:
                globals.scene_manager.register_scene("game", GameScene())
                globals.scene_manager.switch_scene("game")
                
        pygame.draw.rect(globals.screen, play_box_color, (play_box_x, play_box_y, play_box_width, play_box_height))
        play_button = self.button_font.render("Start Game", True, (0, 0, 0))
        globals.screen.blit(play_button, (play_button_x, play_button_y))

        # Add exit button
        exit_button_x = (globals.SCREEN_WIDTH - self.button_font.size("Quit Game")[0]) / 2
        exit_button_y = 550
        exit_button_width = self.button_font.size("Quit Game")[0] 
        exit_button_height = self.button_font.size("Quit Game")[1]

        exit_box_x = exit_button_x - 50
        exit_box_y = exit_button_y - (play_button_height / 2) - 20
        exit_box_width = exit_button_width + 100
        exit_box_height = exit_button_height + exit_button_height + 40 

        exit_box_color = (128, 128, 128)
        
        if mouse_x > exit_box_x and mouse_x < exit_box_x + exit_box_width and mouse_y > exit_box_y and mouse_y < exit_box_y + exit_box_height:
            exit_box_color = (196, 196, 196)
            if self.mouse_prev_pressed and not self.mouse_pressed:
                pygame.quit()
                exit()
        
        pygame.draw.rect(globals.screen, exit_box_color, (exit_box_x, exit_box_y, exit_box_width, exit_box_height))
        exit_button = self.button_font.render("Quit Game", True, (0, 0, 0))
        globals.screen.blit(exit_button, (exit_button_x, exit_button_y))
    
    def switch_to(self):
        # Play music
        pygame.mixer.music.load("./shared/music/title.wav")
        pygame.mixer.music.play(1)

    def handle_events(self, events):        
        pass # Title scene does not handle any events