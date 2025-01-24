import pygame
from .base import DeathAnimatedMob
from tools import create_frames
from config.images import (
    BEE_FLYING_IMAGES,
    BEE_DEATH_IMAGES
)

class Bee(DeathAnimatedMob):
    def __init__(self, x, bottom, speed, ground_left, ground_right):
        super().__init__(x, bottom, BEE_FLYING_IMAGES, BEE_DEATH_IMAGES, 200, 100, speed, ground_left, ground_right)
    

    def copy(self):
        return Bee(self.object_rect.x, self.object_rect.bottom, self.speed, self.ground_left, self.ground_right)