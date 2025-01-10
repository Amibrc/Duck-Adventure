import pygame
from tools import (
    get_display_settings,
    collision_with_objects
)


class MovementDuck():
    def __init__(self, duck_rect : pygame.Rect, states, objects):
        self.duck_rect = duck_rect
        self.states = states
        self.objects = objects

        self.speed_walking = 6
        self.speed_running = 9
        self.speed_crouching = 3

        self.jump_force = 20
        self.vector_speed_vertical = 0
        self.gravity = 2

        self.ground_right, self.ground_bottom = get_display_settings(True, True, False)
        self.on_platform = False
        self.under_platform = False

        self.moved_x = False
        self.moved_y = False

        self.target_rect = duck_rect.copy()


    def move(self, keys, objects):
        if not self.states["is_dead"]:
            if keys[pygame.K_d] and self.duck_rect.right < self.ground_right:
                self.move_right(objects)
            elif self.duck_rect.right > self.ground_right:
                self.duck_rect.right = self.ground_right
                self.target_rect.right = self.ground_right


            if keys[pygame.K_a] and self.duck_rect.left > 0:
                self.move_left(objects)
            elif self.duck_rect.left < 0:
                self.duck_rect.left = 0
                self.target_rect.left = 0

    
    def move_right(self, objects):
        remaining_distance = self.get_speed()
        
        while remaining_distance:
            self.collision_info = collision_with_objects(self.duck_rect, objects)
            for collision_data in self.collision_info:
                if collision_data["object"].type != "prop":
                    if collision_data["collision_sides"]["right"]:
                        self.duck_rect.right = collision_data["obj_rect"].left
                        self.states["direction_right"] = True
                        self.states["direction_left"] = False
                        return
                
            self.duck_rect.right += 1
            self.target_rect.right += 1
            remaining_distance -= 1
        
        self.states["direction_right"] = True
        self.states["direction_left"] = False
                    
    
    def move_left(self, objects):
        remaining_distance = self.get_speed()

        while remaining_distance:
            self.collision_info = collision_with_objects(self.duck_rect, objects)
            for collision_data in self.collision_info:
                if collision_data["object"].type != "prop":
                    if collision_data["collision_sides"]["left"]:
                        self.duck_rect.left = collision_data["obj_rect"].right
                        self.states["direction_left"] = True
                        self.states["direction_right"] = False
                        return
            
            self.duck_rect.left -= 1
            self.target_rect.left -= 1
            remaining_distance -= 1

        self.states["direction_left"] = True
        self.states["direction_right"] = False


    def start_jump(self):
        if not self.states["is_dead"]:
            if self.duck_rect.bottom >= self.ground_bottom - 5:
                if self.states["is_crouching"]:
                    self.vector_speed_vertical = -self.jump_force // 1.5
                else:
                    self.vector_speed_vertical = -self.jump_force
                self.states["is_jumping"] = True

            elif self.duck_rect.bottom < self.ground_bottom - 5 and not self.states["is_jumping"]:
                if self.states["is_crouching"]:
                    self.vector_speed_vertical = -self.jump_force // 1.5
                else:
                    self.vector_speed_vertical = -self.jump_force
                self.states["is_jumping"] = True


    def jumping(self, objects):
        if self.states["is_jumping"]:
            step = 1 if self.vector_speed_vertical > 0 else -1
            remaining_distance = abs(self.vector_speed_vertical)

            while remaining_distance:
                self.duck_rect.bottom += step
                remaining_distance -= 1

                self.collision_info = collision_with_objects(self.duck_rect, objects)

                for collision_data in self.collision_info:
                    if collision_data["object"].type != "prop":
                        if collision_data["on_object"] and self.vector_speed_vertical > 0:
                            self.duck_rect.bottom = collision_data["obj_rect"].top
                            self.target_rect.bottom = collision_data["obj_rect"].top
                            self.vector_speed_vertical = 0
                            self.states["is_jumping"] = False
                            self.on_platform = True
                            return
                        elif collision_data["collision_sides"]["top"] and self.vector_speed_vertical < 0:
                            self.duck_rect.top = collision_data["obj_rect"].bottom
                            self.target_rect.top = collision_data["obj_rect"].bottom
                            self.vector_speed_vertical = 0
                            return
                        self.update_collision_sides_with_static_objects(collision_data)
            
            self.vector_speed_vertical += self.gravity

            if self.duck_rect.bottom + self.vector_speed_vertical >= self.ground_bottom:
                self.duck_rect.bottom = self.ground_bottom
                self.target_rect.bottom = self.ground_bottom
                self.vector_speed_vertical = 0
                self.states["is_jumping"] = False

    
    def update_collisions_and_gravity(self, objects):
        self.collision_info = collision_with_objects(self.duck_rect, objects)
        self.on_platform = False
        self.moved_x = False
        self.moved_y = False

        for collision_data in self.collision_info:
            self.update_collision_sides_with_moved_objects(collision_data)
            self.update_collision_sides_with_static_objects(collision_data)

            self.update_collision_with_mobs(collision_data)

            self.update_collision_with_moved_objects(collision_data)
            self.update_collision_with_static_objects(collision_data)

        self.update_gravity()
    
    
    def update_collision_with_moved_objects(self, collision_data):
        if collision_data["object"].type == "prop":
            if collision_data["collision_x"] and collision_data["collision_y"]:
                collision_data["object"].is_collected = True

        elif collision_data["object"].type == "moved":
            if collision_data["on_object"]:
                if collision_data["object"].speed_x:
                    self.move_horizontally_on_platform(collision_data["object"].speed_x)
                if collision_data["object"].speed_y:
                    self.move_vertically_on_platform(collision_data["object"].speed_y)
                self.on_platform = True
            elif collision_data["collision_sides"]["bottom"]:
                if collision_data["object"].speed_x:
                    self.move_horizontally_on_platform(collision_data["object"].speed_x)
                if collision_data["object"].speed_y:
                    self.duck_rect.bottom = collision_data["obj_rect"].top
                    self.target_rect.bottom = collision_data["obj_rect"].top
                    self.move_vertically_on_platform(collision_data["object"].speed_y)
                    self.vector_speed_vertical = 0
                    self.states["is_jumping"] = False
                self.on_platform = True


    def update_collision_with_static_objects(self, collision_data):
        if collision_data["object"].type == "static":
            if collision_data["on_object"]:
                self.duck_rect.bottom = collision_data["obj_rect"].top
                self.target_rect.bottom = collision_data["obj_rect"].top
                self.vector_speed_vertical = 0
                self.states["is_jumping"] = False
                self.on_platform = True


    def update_collision_with_mobs(self, collision_data):
        if collision_data["object"].type == "mob":
            if collision_data["on_object"] and not self.states["is_dead"]:
                self.duck_rect.bottom = collision_data["obj_rect"].top
                self.target_rect.bottom = collision_data["obj_rect"].top
                collision_data["object"].states["is_dead"] = True
                self.start_jump()
            elif collision_data["collision_sides"]["top"] and not self.states["is_dead"]:
                self.duck_rect.top = collision_data["obj_rect"].bottom
                self.target_rect.top = collision_data["obj_rect"].bottom
                collision_data["object"].states["is_dead"] = True
            elif collision_data["collision_sides"]["right"]:
                self.duck_rect.right = collision_data["obj_rect"].left
                self.target_rect.right = collision_data["obj_rect"].left
                self.states["is_dead"] = True
            elif collision_data["collision_sides"]["left"]:
                self.duck_rect.left = collision_data["obj_rect"].right
                self.target_rect.left = collision_data["obj_rect"].right
                self.states["is_dead"] = True



    def update_collision_sides_with_static_objects(self, collision_data):
        if collision_data["object"].type == "static":
            if collision_data["collision_sides"]["right"]:
                self.duck_rect.right = collision_data["obj_rect"].left
                self.target_rect.right = collision_data["obj_rect"].left
            elif collision_data["collision_sides"]["left"]:
                self.duck_rect.left = collision_data["obj_rect"].right
                self.target_rect.left = collision_data["obj_rect"].right


    def update_collision_sides_with_moved_objects(self, collision_data):
        if collision_data["object"].type == "moved":
            if collision_data["object"].speed_x:
                if collision_data["collision_sides"]["right"]:
                    self.duck_rect.right = collision_data["obj_rect"].left
                    self.target_rect.right = collision_data["obj_rect"].left
                elif collision_data["collision_sides"]["left"]:
                    self.duck_rect.left = collision_data["obj_rect"].right
                    self.target_rect.left = collision_data["obj_rect"].right
            if collision_data["object"].speed_y:
                if collision_data["collision_sides"]["right"] and self.states["is_jumping"]:
                    self.duck_rect.right = collision_data["obj_rect"].left
                    self.target_rect.right = collision_data["obj_rect"].left
                elif collision_data["collision_sides"]["left"] and self.states["is_jumping"]:
                    self.duck_rect.left = collision_data["obj_rect"].right
                    self.target_rect.left = collision_data["obj_rect"].right


    def update_gravity(self):
        if not self.on_platform and not self.states["is_jumping"]:
            self.states["is_jumping"] = True
            self.vector_speed_vertical += self.gravity
            self.duck_rect.bottom += self.vector_speed_vertical
            self.target_rect.bottom += self.vector_speed_vertical

            if self.duck_rect.bottom >= self.ground_bottom:
                self.duck_rect.bottom = self.ground_bottom
                self.target_rect.bottom = self.ground_bottom
                self.vector_speed_vertical = 0
                self.states["is_jumping"] = False
                self.on_platform = True


    def move_horizontally_on_platform(self, speed_x):
        if not self.moved_x:
            remaining_distance = abs(speed_x)
            step = 1 if speed_x > 0 else -1

            while remaining_distance:
                if (self.duck_rect.right < self.ground_right and step > 0) or (self.duck_rect.left > 0 and step < 0):
                    self.duck_rect.x += step
                    self.target_rect.x += step
                    remaining_distance -= 1
                    self.moved_x = True
                else:
                    return
            
            
    def move_vertically_on_platform(self, speed_y):
        if not self.moved_y:
            remaining_distance = abs(speed_y)
            step = 1 if speed_y > 0 else -1

            while remaining_distance:
                if self.duck_rect.bottom < self.ground_bottom:
                    self.duck_rect.y += step
                    self.target_rect.y += step
                    remaining_distance -= 1
                    self.moved_y = True
                else:
                    return
    

    def set_level_size(self, level_width, level_height):
        self.ground_right = level_width
        self.ground_bottom = level_height
            

    def get_speed(self):
        if self.states["is_crouching"]:
            return self.speed_crouching
        elif self.states["is_running"]:
            return self.speed_running
        return self.speed_walking
