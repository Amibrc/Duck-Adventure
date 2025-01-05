import pygame
from background import Background
from duck_classes.duck import Duck
from tools import get_display_settings
from config.paths import FONT_PATH
from config.images import RED_BRICK_IMAGE, GREY_BRICK_IMAGE, STONE_IMAGE, GAME_ICON_IMAGE
from objects.base import StaticObject, MovedObject
from objects.coin import Coin
from objects.diamond import Diamond
from menu import GameMenu

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT, FPS = get_display_settings(True, True, True)

clock = pygame.time.Clock()
game_menu = GameMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

objects = [
    StaticObject(0, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE),
    StaticObject(0, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE),
    StaticObject(182, SCREEN_HEIGHT - 170, GREY_BRICK_IMAGE), StaticObject(214, SCREEN_HEIGHT - 170, GREY_BRICK_IMAGE),
    StaticObject(420, SCREEN_HEIGHT - 250, GREY_BRICK_IMAGE), StaticObject(452, SCREEN_HEIGHT - 250, GREY_BRICK_IMAGE),
    StaticObject(150, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE), StaticObject(182, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE), StaticObject(214, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE), StaticObject(246, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE),
    StaticObject(500, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(500, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
    StaticObject(532, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(532, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE), StaticObject(532, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE),
    StaticObject(564, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(564, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE), StaticObject(564, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(564, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),
    StaticObject(768, SCREEN_HEIGHT - 300, STONE_IMAGE), StaticObject(736, SCREEN_HEIGHT - 300, STONE_IMAGE), StaticObject(704, SCREEN_HEIGHT - 300, STONE_IMAGE), StaticObject(672, SCREEN_HEIGHT - 300, STONE_IMAGE),
    MovedObject(
        x=300,
        bottom=SCREEN_HEIGHT - 50,
        image=GREY_BRICK_IMAGE,
        speed_x=0,
        speed_y=2,
        ground_right=0,
        ground_left=0,
        ground_bottom=SCREEN_HEIGHT,
        ground_top=SCREEN_HEIGHT - 200
    ),
    MovedObject(
        x=332,
        bottom=SCREEN_HEIGHT - 50,
        image=GREY_BRICK_IMAGE,
        speed_x=0,
        speed_y=2,
        ground_right=0,
        ground_left=0,
        ground_bottom=SCREEN_HEIGHT,
        ground_top=SCREEN_HEIGHT - 200
    ),
    MovedObject(
        x=600,
        bottom=SCREEN_HEIGHT - 10,
        image=GREY_BRICK_IMAGE,
        speed_x=2,
        speed_y=0,
        ground_right=SCREEN_WIDTH - 32,
        ground_left=596,
        ground_bottom=0,
        ground_top=0
    ),
    MovedObject(
        x=632,
        bottom=SCREEN_HEIGHT - 10,
        image=GREY_BRICK_IMAGE,
        speed_x=2,
        speed_y=0,
        ground_right=SCREEN_WIDTH,
        ground_left=596+32,
        ground_bottom=0,
        ground_top=0
    ),
    Coin(216, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 30),
    Coin(168, SCREEN_HEIGHT - 72, 0, 1, 0, 0, SCREEN_HEIGHT - 72, SCREEN_HEIGHT - 102),
    Coin(216, SCREEN_HEIGHT - 72, 0, 1, 0, 0, SCREEN_HEIGHT - 72, SCREEN_HEIGHT - 102),
    Coin(264, SCREEN_HEIGHT - 72, 0, 1, 0, 0, SCREEN_HEIGHT - 72, SCREEN_HEIGHT - 102),
    Coin(40, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 30),
    Coin(30, SCREEN_HEIGHT - 260, 0, 1, 0, 0, SCREEN_HEIGHT - 252, SCREEN_HEIGHT - 252-30),
    Diamond(768, SCREEN_HEIGHT - 340, 0, 1, 0, 0, SCREEN_HEIGHT - 332, SCREEN_HEIGHT - 332-40)
]


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Duck Adventure")
pygame.display.set_icon(GAME_ICON_IMAGE)

duck = Duck(SCREEN_WIDTH // 2, SCREEN_HEIGHT, objects)

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
        for obj in objects:
            obj.draw(window)
            if obj.type == "prop" or obj.type == "moved":
                obj.update()
        duck.update(keys, objects)

    elif stage_game == "game_menu":
        game_menu.draw(window)
        stage_game = game_menu.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    
    elif stage_game == "quit":
        game = False

    window.blit(pygame.font.Font(FONT_PATH, 14).render(str(int(clock.get_fps())), True, (0, 255, 0)), (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()