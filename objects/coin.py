from .base import MovedObject, AnimatedObject
from config.images import COIN_IMAGES

class Coin(MovedObject, AnimatedObject):
    def __init__(self, centerx, bottom, speed_x, speed_y, ground_left, ground_right, ground_bottom, ground_top):
        MovedObject.__init__(self, centerx, bottom, None, speed_x, speed_y, ground_left, ground_right, ground_bottom, ground_top, 17)
        AnimatedObject.__init__(self, centerx, bottom, COIN_IMAGES, 300)
        self.is_collected = False
        self.type = "entity"

    
    def update(self):
        MovedObject.update(self)
        AnimatedObject.update_animation(self)

    
    def draw(self, surface):
        AnimatedObject.draw(self, surface)
    

    def copy(self):
        return Coin(self.object_rect.centerx, self.object_rect.bottom, self.speed_x, self.speed_y, self.ground_left, self.ground_right, self.ground_bottom, self.ground_top)
    