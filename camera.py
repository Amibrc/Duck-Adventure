class Camera():
    def __init__(self, width):
        self.width = width
        self.offset_x = 0
        self.offset_y = 0

    
    def update(self, target_x, width):
        self.offset_x = target_x - self.width // 2
        self.offset_x = max(0, min(self.offset_x, width - self.width))

