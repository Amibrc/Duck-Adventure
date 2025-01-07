import pygame

class StaticObject():
    def __init__(self, x, bottom, image):
        self.object_image = image
        self.type = "static"
        if image:
            self.object_rect = self.object_image.get_rect()
            self.object_rect.x = x
            self.object_rect.bottom = bottom

    
    def draw(self, surface):
        surface.blit(self.object_image, self.object_rect)


class MovedObject(StaticObject):
    def __init__(self, x, bottom, image, speed_x, speed_y, ground_left, ground_right, ground_bottom, ground_top, move_interval=0):
        super().__init__(x, bottom, image)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.ground_left = ground_left
        self.ground_right = ground_right
        self.ground_bottom = ground_bottom
        self.ground_top = ground_top
        self.type = "moved"
        self.move_interval = move_interval
        self.last_move_time = 0
    

    def update(self):
        if pygame.time.get_ticks() - self.last_move_time >= self.move_interval:
            if self.speed_x:
                self.object_rect.x += self.speed_x
                if self.object_rect.right > self.ground_right:
                    self.object_rect.right = self.ground_right
                    self.speed_x = -self.speed_x
                elif self.object_rect.left < self.ground_left:
                    self.object_rect.left = self.ground_left
                    self.speed_x = -self.speed_x

            if self.speed_y:
                self.object_rect.y += self.speed_y
                if self.object_rect.bottom > self.ground_bottom:
                    self.object_rect.bottom = self.ground_bottom
                    self.speed_y = -self.speed_y
                elif self.object_rect.top < self.ground_top:
                    self.object_rect.top = self.ground_top
                    self.speed_y = -self.speed_y
            self.last_move_time = pygame.time.get_ticks()


class AnimatedObject():
    def __init__(self, centerx, bottom, animation_frames, animation_interval):
        self.animation_frames = animation_frames
        self.current_frame = 0
        self.current_animation = animation_frames[self.current_frame]
        self.animation_interval = animation_interval
        self.last_animation_time = 0

        self.object_rect = self.current_animation.get_rect(centerx=centerx, bottom=bottom)
        self.type = "animated"
    
    
    def update_animation(self):
        if pygame.time.get_ticks() - self.last_animation_time >= self.animation_interval:
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.current_animation = self.animation_frames[self.current_frame]
            self.object_rect = self.current_animation.get_rect(centerx=self.object_rect.centerx, bottom=self.object_rect.bottom)
            self.last_animation_time = pygame.time.get_ticks()

    
    def draw(self, surface):
        surface.blit(self.current_animation, self.object_rect)