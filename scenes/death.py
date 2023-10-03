# Title Scene
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)
import pygame
import globals

from utils.scene import SceneBase

class DeathScene(SceneBase):
    def __init__(self, score):
        self.title_font = pygame.font.Font("./shared/fonts/Pixeboy.ttf", 128)
        self.button_font = pygame.font.Font("./shared/fonts/Pixeboy.ttf", 40)
        self.mouse_pressed = False
        self.mouse_prev_pressed = False
        self.score = score

    def update(self, dt):
        self.dt = dt
        self.mouse_prev_pressed = self.mouse_pressed
        self.mouse_pressed = pygame.mouse.get_pressed()[0]
        pass

    def render(self):
        # Clear screen
        globals.screen.fill((0, 0, 0))

        # Draw title
        title = self.title_font.render("YOU DIED", True, (255, 0, 0))
        globals.screen.blit(title, ((globals.SCREEN_WIDTH - self.title_font.size("YOU DIED")[0]) / 2, 76))

        # Draw subtitle
        subtitle = self.button_font.render(f"Score: {self.score}", True, (255, 255, 255))
        globals.screen.blit(subtitle, ((globals.SCREEN_WIDTH - self.button_font.size(f"Score: {self.score}")[0]) / 2, 170))

        # Cursor Position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Add play button
        play_button_x = (globals.SCREEN_WIDTH - self.button_font.size("Main Menu")[0]) / 2
        play_button_y = 350
        play_button_width = self.button_font.size("Main Menu")[0] 
        play_button_height = self.button_font.size("Main Menu")[1]

        play_box_x = play_button_x - 50
        play_box_y = play_button_y - (play_button_height / 2) - 20
        play_box_width = play_button_width + 100
        play_box_height = play_button_height + play_button_height + 40

        play_box_color = (128, 128, 128)

        if mouse_x > play_box_x and mouse_x < play_box_x + play_box_width and mouse_y > play_box_y and mouse_y < play_box_y + play_box_height:
            play_box_color = (196, 196, 196)
            if self.mouse_prev_pressed and not self.mouse_pressed:
                globals.scene_manager.switch_scene("title")
                
        pygame.draw.rect(globals.screen, play_box_color, (play_box_x, play_box_y, play_box_width, play_box_height))
        play_button = self.button_font.render("Main Menu", True, (0, 0, 0))
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

    def handle_events(self, events):        
        pass # Title scene does not handle any events