from .base import MovedObject, AnimatedObject
from config.images import DIAMOND_IMAGES

class Diamond(MovedObject, AnimatedObject):
    def __init__(self, centerx, bottom, speed_x, speed_y, ground_left, ground_right, ground_bottom, ground_top):
        MovedObject.__init__(self, centerx, bottom, None, speed_x, speed_y, ground_left, ground_right, ground_bottom, ground_top, 30)
        AnimatedObject.__init__(self, centerx, bottom, DIAMOND_IMAGES, 400)
        self.is_collected = False
        self.type = "prop"
    
    
    def update(self):
        MovedObject.update(self)
        AnimatedObject.update_animation(self)


    def draw(self, surface):
        AnimatedObject.draw(self, surface)