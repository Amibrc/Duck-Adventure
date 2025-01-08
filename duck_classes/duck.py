import pygame
from .animator import AnimatorDuck
from .movement import MovementDuck

class Duck():
    def __init__(self, centerx, bottom, objects):
        self.centerx = centerx
        self.bottom = bottom

        self.states = {
            "direction_right": True,
            "direction_left": False,
            "is_idle": True,
            "is_middle_idle": False,
            "is_walking": False,
            "is_running": False,
            "is_crouching": False,
            "is_jumping": False,
            "is_rude": False,
            "is_dead": False
        }

        self.Animator = AnimatorDuck(self.states)
        self.duck_rect = self.Animator.animation_frames["idle"]["right"][0].get_rect(centerx=self.centerx, bottom=self.bottom)
        self.current_frame_duck = self.Animator.animation_frames["idle"]["right"][0]
        self.Movement = MovementDuck(self.duck_rect, self.states, objects)

        
    def update(self, keys, objects):
        #print(self.states["direction_right"], self.states["direction_left"], self.states["is_jumping"])
        self.update_animation() # 1. update_animation
        self.Movement.move(keys, objects) # 2. move
        self.Movement.jumping(objects) # 3. jumping
        self.update_states(keys, objects) # 4. update_states
        

    def update_animation(self):
        self.current_frame_duck = self.Animator.animate_duck(self.current_frame_duck)
    

    def update_duck_rect(self):
        self.bottom = self.duck_rect.bottom
        self.centerx = self.duck_rect.centerx
        right = self.duck_rect.right
        left = self.duck_rect.left

        current_rect = self.current_frame_duck.get_rect(centerx=self.centerx, bottom=self.bottom)

        self.duck_rect.width = current_rect.width
        self.duck_rect.height = current_rect.height
        self.duck_rect.bottom = self.bottom

        if self.states["direction_right"]:
            self.duck_rect.right = right
        elif self.states["direction_left"]:
            self.duck_rect.left = left


    def update_states(self, keys, objects):
        self.states["is_middle_idle"] = keys[pygame.K_d] and keys[pygame.K_a] and not self.states["is_dead"]
        self.states["is_walking"] = not self.states["is_middle_idle"] and not keys[pygame.K_LSHIFT] and (keys[pygame.K_d] or keys[pygame.K_a]) and not self.states["is_dead"]
        self.states["is_running"] = not self.states["is_middle_idle"] and keys[pygame.K_LSHIFT] and (keys[pygame.K_d] or keys[pygame.K_a]) and not keys[pygame.K_LCTRL] and not self.states["is_dead"]
        self.states["is_crouching"] = keys[pygame.K_LCTRL] and not self.states["is_dead"]
        self.states["is_rude"] = keys[pygame.K_f] and not self.states["is_dead"]
        self.states["is_idle"] = not (self.states["is_walking"] or self.states["is_running"] or self.states["is_crouching"] or self.states["is_jumping"] or self.states["is_middle_idle"] or self.states["is_rude"] or self.states["is_dead"] or self.states["is_dead"])

        self.update_duck_rect()
        self.Movement.update_collisions_and_gravity(objects)
    

    def set_objects(self, objects):
        self.Movement.objects = objects

    
    def set_position(self, centerx, bottom):
        self.duck_rect.centerx = centerx
        self.duck_rect.bottom = bottom
        self.update_duck_rect()


    def draw(self, surface, camera):
        surface.blit(self.current_frame_duck, camera.apply(self.duck_rect))