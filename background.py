import pygame
from tools import scale_image_to_screen
from config.images import BACKGROUND_STATIC_IMAGES, BACKGROUND_SCROLL_IMAGES

class Background():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background = pygame.Surface((width, height))
        self.background_rect = self.background.get_rect()
        self.layers_static = tuple(scale_image_to_screen(image, width, height) for image in BACKGROUND_STATIC_IMAGES)
        self.layers_scroll = tuple(scale_image_to_screen(image, width, height) for image in BACKGROUND_SCROLL_IMAGES)
        self.layers = self.layers_static + self.layers_scroll
        for layer in self.layers:
            self.background.blit(layer, (0, 0))


    def draw(self, surface):
        surface.blit(self.background, self.background_rect)


    def update_to_videoresize(self, width, height):
        self.width, self.height = width, height
        self.background = pygame.Surface((width, height))
        self.background_rect = self.background.get_rect()
        self.layers_static = tuple(scale_image_to_screen(layer, width, height) for layer in self.layers_static)
        self.layers_scroll = tuple(scale_image_to_screen(layer, width, height) for layer in self.layers_scroll)
        self.layers = self.layers_static + self.layers_scroll
        for layer in self.layers:
            self.background.blit(layer, (0, 0))

        