import pygame
from background import Background
from duck_classes.duck import Duck
from tools import get_display_settings
from config.paths import FONT_PATH
from config.images import GAME_ICON_IMAGE
from levels import level_test
from menu import GameMenu

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT, FPS = get_display_settings(True, True, True)

clock = pygame.time.Clock()
game_menu = GameMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Duck Adventure")
pygame.display.set_icon(GAME_ICON_IMAGE)

duck = Duck(SCREEN_WIDTH // 2, SCREEN_HEIGHT, level_test.all_objects)

stage_game = "game_menu"
game = True
while game:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stage_game = "game_menu"
            elif event.key == pygame.K_SPACE and stage_game == "playing":
                duck.Movement.start_jump()
    
    if stage_game == "playing":
        background.draw(window)
        duck.draw(window)
        level_test.draw(window)
        level_test.update()
        duck.update(keys, level_test.all_objects)

    elif stage_game == "game_menu":
        game_menu.draw(window)
        stage_game = game_menu.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    
    elif stage_game == "quit":
        game = False

    window.blit(pygame.font.Font(FONT_PATH, 14).render(str(int(clock.get_fps())), True, (0, 255, 0)), (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()