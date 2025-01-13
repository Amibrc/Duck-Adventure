from .base import Entity
from config.images import DIAMOND_IMAGES

class Diamond(Entity):
    def __init__(self, centerx, bottom, speed_x, speed_y, ground_left, ground_right, ground_bottom, ground_top):
        super().__init__(centerx, bottom, DIAMOND_IMAGES, 400, speed_x, speed_y, ground_left, ground_right, ground_bottom, ground_top, 30)
    

    def copy(self):
        return Diamond(self.object_rect.centerx, self.object_rect.bottom, self.speed_x, self.speed_y, self.ground_left, self.ground_right, self.ground_bottom, self.ground_top)