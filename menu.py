import pygame
from tools import scale_images
from config.images import START_BUTTON_IMAGES, SETTINGS_BUTTON_IMAGES, QUIT_BUTTON_IMAGES

class GameMenu():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background = self.create_background(width, height)

        self.start_buttons = scale_images(START_BUTTON_IMAGES, (280, 120))
        self.settings_buttons = scale_images(SETTINGS_BUTTON_IMAGES, (103 * 4, 120))
        self.quit_buttons = scale_images(QUIT_BUTTON_IMAGES, (220, 120))

        self.current_start_button = self.start_buttons[0]
        self.current_settings_button = self.settings_buttons[0]
        self.current_quit_button = self.quit_buttons[0]

        self.current_start_button_rect = self.start_buttons[0].get_rect(center=(self.width // 2, self.height // 3))
        self.current_settings_button_rect = self.settings_buttons[0].get_rect(center=(self.width // 2, self.height // 1.7))
        self.current_quit_button_rect = self.quit_buttons[0].get_rect(center=(self.width // 2, self.height // 1.2))

        self.pressed_button = None
        self.last_pressed_button_time = 0
        self.animation_button_time = 1000


    def draw(self, surface):
        self.background.fill((255, 255, 255))
        self.background.blit(self.current_start_button, self.current_start_button_rect)
        self.background.blit(self.current_settings_button, self.current_settings_button_rect)
        self.background.blit(self.current_quit_button, self.current_quit_button_rect)
        surface.blit(self.background, (0, 0))


    def create_background(self, width, height):
        background = pygame.Surface((width, height))
        background.fill((255, 255, 255))
        return background


    def update(self, mouse_pos, mouse_pressed):
        start_button_state = self.update_button_state(mouse_pos, mouse_pressed, self.start_buttons, self.current_start_button_rect)
        if start_button_state == "static":
            self.current_start_button = self.start_buttons[0]
        elif start_button_state == "hover":
            self.current_start_button = self.start_buttons[1]
        else:
            self.current_start_button = self.start_buttons[2]
            return "playing"
            
        quit_button_state = self.update_button_state(mouse_pos, mouse_pressed, self.quit_buttons, self.current_quit_button_rect)
        if quit_button_state == "static":
            self.current_quit_button = self.quit_buttons[0]
                
        elif quit_button_state == "hover":
            self.current_quit_button = self.quit_buttons[1]
        else:
            self.current_quit_button = self.quit_buttons[2]
            return "quit"
            
        settings_button_state = self.update_button_state(mouse_pos, mouse_pressed, self.settings_buttons, self.current_settings_button_rect)
        if settings_button_state == "static":
            self.current_settings_button = self.settings_buttons[0]
        elif settings_button_state == "hover":
            self.current_settings_button = self.settings_buttons[1]
        else:
            self.current_settings_button = self.settings_buttons[2]
            #return "settings"

        return "game_menu"

    
    def update_button_state(self, mouse_pos, mouse_pressed, buttons, current_rect):
        if current_rect.collidepoint(mouse_pos):
            if mouse_pressed[0]:
                self.pressed_button = buttons[1]
                return "pressed"
            else:
                return "hover"
        else:
            return "static"

    