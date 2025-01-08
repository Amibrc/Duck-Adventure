import pygame
from tools import scale_image_to_screen
from config.images import (
    BACKGROUND_STATIC_IMAGES,
    BACKGROUND_SCROLL_IMAGES
)

class Background():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background = pygame.Surface((width, height))
        self.layers_static = tuple(scale_image_to_screen(image, width, height) for image in BACKGROUND_STATIC_IMAGES)
        self.layers_scroll = tuple(scale_image_to_screen(image, width, height) for image in BACKGROUND_SCROLL_IMAGES)
        self.layers = self.layers_static + self.layers_scroll
        self.scroll_speeds = (0.025, 0.05, 0.1)

        for layer in self.layers:
            self.background.blit(layer, (0, 0))


    def draw(self, surface):
        surface.blit(self.background, (0, 0))


    def update(self, camera):
        self.background.fill((0, 0, 0))

        for layer in self.layers_static:
            self.background.blit(layer, (0, 0))

        for i, layer in enumerate(self.layers_scroll):
            scroll_x = -camera.offset_x * self.scroll_speeds[i]
            scroll_y = -camera.offset_y * self.scroll_speeds[i]
            self.background.blit(layer, (scroll_x, scroll_y))



        