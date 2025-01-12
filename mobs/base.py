
class Mob():
    def __init__(self, speed, ground_left, ground_right):
        self.speed = speed
        self.ground_left = ground_left
        self.ground_right = ground_right
        self.death_animation_ended = False
        self.type = "mob"

        self.states  = {
            "direction_right": speed > 0,
            "direction_left": speed < 0,
            "is_walking": True,
            "is_dead": False
        }
    
    
    def get_direction(self):
        if self.states["direction_right"]:
            return "right"
        elif self.states["direction_left"]:
            return "left"
        