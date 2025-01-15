from .base import SimpleMob
from config.images import ROYAL_SCARAB_WALKING_IMAGES

class RoyalScarab(SimpleMob):
    def __init__(self, x, bottom, speed, ground_left, ground_right):
        super().__init__(x, bottom, ROYAL_SCARAB_WALKING_IMAGES, 150, speed, ground_left, ground_right)

    def copy(self):
        return RoyalScarab(self.object_rect.x, self.object_rect.bottom, self.speed, self.ground_left, self.ground_right)