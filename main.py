import pygame
from background import Background
from duck_classes.duck import Duck
from tools import get_display_settings
from config.paths import FONT_PATH
from config.images import GAME_ICON_IMAGE
from levels import level_manager
from menu import GameMenu
from camera import Camera

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT, FPS = get_display_settings(True, True, True)

clock = pygame.time.Clock()
game_menu = GameMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Duck Adventure")
pygame.display.set_icon(GAME_ICON_IMAGE)

duck = Duck(80, SCREEN_HEIGHT, level_manager.all_level_objects)
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

stage_game = "game_menu"
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stage_game = "game_menu"
            elif event.key == pygame.K_SPACE and stage_game == "playing":
                duck.Movement.start_jump()
    
    if stage_game == "playing":
        keys = pygame.key.get_pressed()

        background.draw(window)
        duck.draw(window, camera)
        level_manager.draw(window, camera)
        
        if level_manager.check_diamond():
            duck.set_objects(level_manager.all_level_objects)
            duck.set_position(10, SCREEN_HEIGHT)

        duck.update(keys, level_manager.all_level_objects)
        camera.update(duck.duck_rect, level_manager.current_level.level_width, level_manager.current_level.level_height)
        duck.Movement.ground_right = level_manager.current_level.level_width
        level_manager.update()
        background.update(camera)

    elif stage_game == "game_menu":
        game_menu.draw(window)
        stage_game = game_menu.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    
    elif stage_game == "quit":
        game = False

    window.blit(pygame.font.Font(FONT_PATH, 14).render(str(int(clock.get_fps())), True, (0, 255, 0)), (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()