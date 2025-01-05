import pygame
from tools import create_frames
from config.images import (
    DUCK_IDLE_IMAGES,
    DUCK_MIDDLE_IDLE_IMAGES,
    DUCK_CROUCHING_IDLE_IMAGE,
    DUCK_WALKING_IMAGES,
    DUCK_RUNNING_IMAGES,
    DUCK_CROUCHING_IMAGES,
    DUCK_JUMPING_IMAGE,
    DUCK_RUDE_IMAGE,
    DUCK_DEAD_IMAGE
)

class AnimatorDuck():
    def __init__(self, states):
        self.states = states

        self.animation_frames = {
            "idle": create_frames(DUCK_IDLE_IMAGES),
            "middle_idle": {
                "middle": DUCK_MIDDLE_IDLE_IMAGES,
            },
            "crouching_idle": create_frames(DUCK_CROUCHING_IDLE_IMAGE),
            "walking": create_frames(DUCK_WALKING_IMAGES),
            "running": create_frames(DUCK_RUNNING_IMAGES),
            "crouching": create_frames(DUCK_CROUCHING_IMAGES),
            "jumping": create_frames(DUCK_JUMPING_IMAGE),
            "rude": create_frames(DUCK_RUDE_IMAGE),
            "dead": create_frames(DUCK_DEAD_IMAGE)
        }

        self.current_frames = {
            "idle": 0,
            "middle_idle": 0,
            "walking": 0,
            "running": 0,
            "crouching_walk": 0
        }

        self.last_animation_idle_time = 0
        self.last_animation_middle_idle_time = 0
        self.last_animation_walking_time = 0
        self.last_animation_running_time = 0
        self.last_animation_crouching_walk_time = 0

        self.animation_idle_interval = 350
        self.animation_middle_idle_interval = 350
        self.animation_walking_interval = 180
        self.animation_running_interval = 120
        self.animation_crouching_walk_interval = 350


    def animate_duck(self, current_frame_duck):
        if self.states["is_idle"]:
            self.reset_animation_frames("idle")
            return self.idle_animation(current_frame_duck)
        
        elif self.states["is_crouching"]:
            if self.states["is_jumping"]:
                self.reset_animation_frames()
                return self.crouching_jump_animation()
            elif self.states["is_walking"]:
                self.reset_animation_frames("crouching_walk")
                return self.crouching_walk_animation(current_frame_duck)
            else:
                self.reset_animation_frames()
                return self.crouching_idle_animation()
        
        elif self.states["is_middle_idle"]:
            if self.states["is_jumping"]:
                self.reset_animation_frames()
                return self.animation_frames["middle_idle"]["middle"][0]
            self.reset_animation_frames("middle_idle")
            return self.middle_idle_animation(current_frame_duck)
        
        elif self.states["is_jumping"]:
            self.reset_animation_frames()
            return self.jumping_animation()

        elif self.states["is_walking"]:
            self.reset_animation_frames("walking")
            return self.walking_animation(current_frame_duck)
        
        elif self.states["is_running"]:
            self.reset_animation_frames("running")
            return self.running_animation(current_frame_duck)
        
        elif self.states["is_rude"]:
            self.reset_animation_frames()
            return self.rude_animation()
        
        elif self.states["is_dead"]:
            self.reset_animation_frames()
            return self.dead_animation()
        
        return current_frame_duck


    def get_direction(self):
        if self.states["direction_right"]:
            return "right"
        elif self.states["direction_left"]:
            return "left"


    def idle_animation(self, current_frame_duck):
        frames = self.animation_frames["idle"][self.get_direction()]

        if pygame.time.get_ticks() - self.last_animation_idle_time >= self.animation_idle_interval:
            self.current_frames["idle"] = (self.current_frames["idle"] + 1) % len(frames)
            current_frame_duck = frames[self.current_frames["idle"]]
            self.last_animation_idle_time = pygame.time.get_ticks()
        return current_frame_duck
    

    def middle_idle_animation(self, current_frame_duck):
        frames = self.animation_frames["middle_idle"]["middle"]

        if pygame.time.get_ticks() - self.last_animation_middle_idle_time >= self.animation_middle_idle_interval:
            self.current_frames["middle_idle"] = (self.current_frames["middle_idle"] + 1) % len(frames)
            current_frame_duck = frames[self.current_frames["middle_idle"]]
            self.last_animation_middle_idle_time = pygame.time.get_ticks()
        return current_frame_duck
    

    def crouching_walk_animation(self, current_frame_duck):
        frames = self.animation_frames["crouching"][self.get_direction()]

        if pygame.time.get_ticks() - self.last_animation_crouching_walk_time >= self.animation_crouching_walk_interval:
            self.current_frames["crouching_walk"] = (self.current_frames["crouching_walk"] + 1) % len(frames)
            current_frame_duck = frames[self.current_frames["crouching_walk"]]
            self.last_animation_crouching_walk_time = pygame.time.get_ticks()
        else:
            current_frame_duck = frames[self.current_frames["crouching_walk"]]
        return current_frame_duck


    def walking_animation(self, current_frame_duck):
        frames = self.animation_frames["walking"][self.get_direction()]

        if pygame.time.get_ticks() - self.last_animation_walking_time >= self.animation_walking_interval:
            self.current_frames["walking"] = (self.current_frames["walking"] + 1) % len(frames)
            current_frame_duck = frames[self.current_frames["walking"]]
            self.last_animation_walking_time = pygame.time.get_ticks()
        else:
            current_frame_duck = frames[self.current_frames["walking"]]
        return current_frame_duck
    

    def running_animation(self, current_frame_duck):
        frames = self.animation_frames["running"][self.get_direction()]
 
        if pygame.time.get_ticks() - self.last_animation_running_time >= self.animation_running_interval:
            self.current_frames["running"] = (self.current_frames["running"] + 1) % len(frames)
            current_frame_duck = frames[self.current_frames["running"]]
            self.last_animation_running_time = pygame.time.get_ticks()
        else:
            current_frame_duck = frames[self.current_frames["running"]]
        return current_frame_duck
    

    def crouching_jump_animation(self):
        if self.states["is_walking"]:
            return self.animation_frames["crouching"][self.get_direction()][0]
        return self.animation_frames["crouching_idle"][self.get_direction()]
        

    def jumping_animation(self):
        return self.animation_frames["jumping"][self.get_direction()]


    def crouching_idle_animation(self):
        return self.animation_frames["crouching_idle"][self.get_direction()]


    def rude_animation(self):
        return self.animation_frames["rude"][self.get_direction()]

    
    def dead_animation(self):
        return self.animation_frames["dead"][self.get_direction()]


    def reset_animation_frames(self, excluded_animation=None):
        for animation in self.current_frames:
            if animation != excluded_animation:
                self.current_frames[animation] = 1

