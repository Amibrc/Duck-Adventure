import pygame
from tools import create_frames

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


class SimpleMob(Mob):
    def __init__(self, x, bottom, walking_images, animation_walking_interval, speed, ground_left, ground_right):
        super().__init__(speed, ground_left, ground_right)

        self.animation_frames = {
            "walking": create_frames(walking_images),
            "death": create_frames(tuple(pygame.transform.flip(img, False, True) for img in walking_images))
        }

        self.walking_frame = 0

        self.current_frame_mob = self.animation_frames["walking"]["right"][0]
        self.object_rect = self.current_frame_mob.get_rect(x=x, bottom=bottom)

        self.animation_walking_interval = animation_walking_interval
        self.animation_death_interval = 1300

        self.last_animation_walking_time = 0
        self.last_animation_death_time = 0

        self.death_animation_ended = False

        self.jump_force = 10
        self.vector_speed_vertical = 0
        self.gravity = 1
    

    def draw(self, surface):
        surface.blit(self.current_frame_mob, self.object_rect)
    

    def update(self):
        if not self.states["is_dead"]:
            self.update_walking_animation()
            self.move()
        else:
            self.update_death_animation()


    def update_walking_animation(self):
        frames = self.animation_frames["walking"][self.get_direction()]

        if pygame.time.get_ticks() - self.last_animation_walking_time >= self.animation_walking_interval:
            self.walking_frame = (self.walking_frame + 1) % len(frames)
            self.current_frame_mob = frames[self.walking_frame]
            self.object_rect = self.current_frame_mob.get_rect(centerx=self.object_rect.centerx, bottom=self.object_rect.bottom)
            self.last_animation_walking_time = pygame.time.get_ticks()
            self.last_animation_death_time = pygame.time.get_ticks()
    

    def update_death_animation(self):
        if self.vector_speed_vertical + self.gravity == 0:
            self.vector_speed_vertical += self.gravity * 2
        elif self.vector_speed_vertical:
            self.object_rect.bottom += self.vector_speed_vertical
            self.vector_speed_vertical += self.gravity
        else:
            self.vector_speed_vertical = -self.jump_force

        self.current_frame_mob = self.animation_frames["death"][self.get_direction()][self.walking_frame]
        if pygame.time.get_ticks() - self.last_animation_death_time >= self.animation_death_interval:
            self.death_animation_ended = True


    def move(self):
        if self.object_rect.right + self.speed >= self.ground_right:
            self.object_rect.right = self.ground_right
            self.speed = -self.speed
            self.states["direction_right"] = not self.states["direction_right"]
            self.states["direction_left"] = not self.states["direction_left"]
        elif self.object_rect.left + self.speed <= self.ground_left:
            self.object_rect.left = self.ground_left
            self.speed = -self.speed
            self.states["direction_right"] = not self.states["direction_right"]
            self.states["direction_left"] = not self.states["direction_left"]
        else:
            self.object_rect.x += self.speed


        