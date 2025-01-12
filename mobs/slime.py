import pygame
from .base import Mob
from tools import create_frames
from config.images import (
    SLIME_WALKING_IMAGES,
    SLIME_DEATH_IMAGES
)

class Slime(Mob):
    def __init__(self, x, bottom, speed, ground_left, ground_right):
        super().__init__(speed, ground_left, ground_right)

        self.animation_frames = {
            "walking": create_frames(SLIME_WALKING_IMAGES),
            "death": create_frames(SLIME_DEATH_IMAGES)
        }

        self.current_frames = {
            "walking": 0,
            "death": 0
        }

        self.current_frame_mob = self.animation_frames["walking"]["right"][0]
        self.object_rect = self.current_frame_mob.get_rect(x=x, bottom=bottom)

        self.last_animation_walking_time = 0
        self.last_animation_death_time = 0

        self.animation_walking_interval = 200
        self.animation_death_interval = 100


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
            self.current_frames["walking"] = (self.current_frames["walking"] + 1) % len(frames)
            self.current_frame_mob = frames[self.current_frames["walking"]]
            self.object_rect = self.current_frame_mob.get_rect(centerx=self.object_rect.centerx, bottom=self.object_rect.bottom)
            self.last_animation_walking_time = pygame.time.get_ticks()
    

    def update_death_animation(self):
        frames = self.animation_frames["death"][self.get_direction()]

        if self.current_frames["death"] < len(frames) - 1:
            if pygame.time.get_ticks() - self.last_animation_death_time >= self.animation_death_interval:
                self.object_rect = frames[self.current_frames["death"]].get_rect(centerx=self.object_rect.centerx, bottom=self.object_rect.bottom)
                self.current_frame_mob = frames[self.current_frames["death"]]
                self.current_frames["death"] += 1
                self.last_animation_death_time = pygame.time.get_ticks()
        else:
            self.death_animation_ended = True


    def move(self):
        if self.object_rect.right + self.speed > self.ground_right:
            self.object_rect.right = self.ground_right
            self.speed = -self.speed
            self.states["direction_right"] = not self.states["direction_right"]
            self.states["direction_left"] = not self.states["direction_left"]
        elif self.object_rect.left + self.speed < self.ground_left:
            self.object_rect.left = self.ground_left
            self.speed = -self.speed
            self.states["direction_right"] = not self.states["direction_right"]
            self.states["direction_left"] = not self.states["direction_left"]
        else:
            self.object_rect.x += self.speed


    def copy(self):
        return Slime(self.object_rect.x, self.object_rect.bottom, self.speed, self.ground_left, self.ground_right)

        
    

