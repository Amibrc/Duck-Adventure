from config import SLIME_WALKING_PATH, SLIME_DEATH_PATH

class Slime():
    def __init__(self, centerx, bottom, ground_left, ground_right):
        self.centerx = centerx
        self.bottom = bottom
        self.ground_left = ground_left
        self.ground_right = ground_right
        self.speed = 2
        self.type = "slime"
        self.alive = True


    def move(self):
        self.centerx += self.speed
        if self.centerx < self.ground_left or self.centerx > self.ground_right:
            self.speed = -self.speed
        
    

