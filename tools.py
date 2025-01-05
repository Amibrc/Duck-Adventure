import pygame
from json import load
from config.paths import DISPLAY_CONFIG_PATH


def calculate_scale_factor(screen_width, screen_height, new_screen_width, new_screen_height):
    return min(new_screen_width / screen_width, new_screen_height / screen_height)


def scale_animations(original_animation_frames, current_animation_frames, scale_factor):
    for state, directions in original_animation_frames.items():
        for direction, frames in directions.items():
            if isinstance(frames, tuple):
                current_animation_frames[state][direction] = tuple(pygame.transform.scale(frame, (frame.get_width() * scale_factor, frame.get_height() * scale_factor)) for frame in frames)
            else:
                current_animation_frames[state][direction] = pygame.transform.scale(frames, (frames.get_width() * scale_factor, frames.get_height() * scale_factor))
    return current_animation_frames


def scale_image_to_screen(image, width, height):
    scale_max = max(width / image.get_width(), height / image.get_height())
    return pygame.transform.scale(image, (int(image.get_width() * scale_max), int(image.get_height() * scale_max)))


def get_display_settings(get_width, get_height, get_max_fps):
    info = []
    with open(DISPLAY_CONFIG_PATH, "r") as config:
        data = load(config)
    if get_width:
        info.append(data["SAVED_SCREEN_WIDTH"])
    if get_height:
        info.append(data["SAVED_SCREEN_HEIGHT"])
    if get_max_fps:
        info.append(data["SAVED_FPS_MAX"])
    return info


def collision_with_objects(character_rect, objects):
    collision_objects = []
    for obj in objects:
        obj_rect = obj.object_rect
        
        if obj.type == "prop":
            collision_x = character_rect.right >= obj_rect.left and character_rect.left <= obj_rect.right
            collision_y = character_rect.bottom >= obj_rect.top and character_rect.top <= obj_rect.bottom

            if collision_x and collision_y:
                collision_data = {
                    "object": obj,
                    "obj_rect": obj_rect,
                    "collision_x": collision_x,
                    "collision_y": collision_y
                }
                collision_objects.append(collision_data)
        else:
            collision_x = character_rect.right > obj_rect.left and character_rect.left < obj_rect.right
            collision_y = character_rect.bottom > obj_rect.top and character_rect.top < obj_rect.bottom
            on_object = collision_x and character_rect.bottom == obj_rect.top

            if collision_x and collision_y or on_object:
                collision_data = {
                    "object": obj,
                    "obj_rect": obj_rect,
                    "on_object": on_object,
                    "collision_x": collision_x,
                    "collision_y": collision_y,
                    "collision_sides": {
                        "right": collision_y and character_rect.right > obj_rect.left and character_rect.right < obj_rect.right,
                        "left": collision_y and character_rect.left < obj_rect.right and character_rect.left > obj_rect.left,
                        "top": obj_rect.top < character_rect.top < obj_rect.bottom and character_rect.bottom > obj_rect.bottom,
                        "bottom": character_rect.bottom > obj_rect.top and character_rect.bottom < obj_rect.bottom
                    }
                }

                collision_objects.append(collision_data)
    
    return collision_objects


def create_frames(images):
    if isinstance(images, tuple):
        frames = {
            "right": images,
            "left": tuple(pygame.transform.flip(image, True, False) for image in images)
        }
    else:
        frames = {
            "right": images,
            "left": pygame.transform.flip(images, True, False)
        }
    return frames


def load_images(paths):
    return tuple(pygame.image.load(path) for path in paths)


def load_and_scale_images(paths, size):
    return tuple(pygame.transform.scale(pygame.image.load(path), size) for path in paths)


def scale_images(images, size):
    return tuple(pygame.transform.scale(image, size) for image in images)





