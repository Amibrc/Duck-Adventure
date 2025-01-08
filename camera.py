
class Camera():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0

    
    def update(self, target_rect, level_width, level_height):
        self.offset_x = target_rect.centerx - self.width // 2
        self.offset_y = target_rect.centery - self.height // 2

        self.offset_x = max(0, min(self.offset_x, level_width - self.width))
        self.offset_y = max(0, min(self.offset_y, level_height - self.height))
    

    def apply(self, target_rect):
        return target_rect.move(-self.offset_x, -self.offset_y)
