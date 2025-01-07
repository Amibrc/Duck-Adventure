from objects.base import *
from objects.coin import Coin
from objects.diamond import Diamond
from mobs.slime import Slime
from tools import get_display_settings
from config.images import (
    RED_BRICK_IMAGE,
    GREY_BRICK_IMAGE,
    STONE_IMAGE
)

class Level():
    def __init__(self, objects, enemies, coins, diamonds):
        self.all_objects = objects + enemies + coins + diamonds
        self.objects = objects
        self.enemies = enemies
        self.coins = coins
        self.diamonds = diamonds
        
    
    def draw(self, surface):
        for obj in self.objects:
            obj.draw(surface)

        for enemy in self.enemies:
            enemy.draw(surface)

        for coin in self.coins:
            coin.draw(surface)
        
        for diamond in self.diamonds:
            diamond.draw(surface)
    

    def update(self):
        for obj in self.objects:
            if obj.type == 'moved':
                obj.update()

        for enemy in self.enemies:
            enemy.update()
            if enemy.death_animation_ended:
                self.enemies.remove(enemy)
                self.all_objects.remove(enemy)

        for coin in self.coins:
            coin.update()
            if coin.is_collected:
                self.coins.remove(coin)
                self.all_objects.remove(coin)
            
        for diamond in self.diamonds:
            diamond.update()
            if diamond.is_collected:
                self.diamonds.remove(diamond)
                self.all_objects.remove(diamond)

SCREEN_WIDTH, SCREEN_HEIGHT = get_display_settings(True, True, False)

level_test = Level(
    objects=[
        StaticObject(0, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE),
        StaticObject(0, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE),
        #StaticObject(182, SCREEN_HEIGHT - 170, GREY_BRICK_IMAGE), StaticObject(214, SCREEN_HEIGHT - 170, GREY_BRICK_IMAGE),
        StaticObject(420, SCREEN_HEIGHT - 250, GREY_BRICK_IMAGE), StaticObject(452, SCREEN_HEIGHT - 250, GREY_BRICK_IMAGE),
        StaticObject(150, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE), StaticObject(182, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE), StaticObject(214, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE), StaticObject(246, SCREEN_HEIGHT - 40, RED_BRICK_IMAGE),
        StaticObject(500, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(500, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(532, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(532, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE), StaticObject(532, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE),
        StaticObject(564, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(564, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE), StaticObject(564, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(564, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),
        StaticObject(768, SCREEN_HEIGHT - 300, STONE_IMAGE), StaticObject(736, SCREEN_HEIGHT - 300, STONE_IMAGE), StaticObject(704, SCREEN_HEIGHT - 300, STONE_IMAGE), StaticObject(672, SCREEN_HEIGHT - 300, STONE_IMAGE),
        MovedObject(300, SCREEN_HEIGHT - 50, GREY_BRICK_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 200),
        MovedObject(332, SCREEN_HEIGHT - 50, GREY_BRICK_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 200),
        MovedObject(600, SCREEN_HEIGHT - 10, GREY_BRICK_IMAGE, 2, 0, 596, SCREEN_WIDTH - 32, 0, 0),
        MovedObject(632, SCREEN_HEIGHT - 10, GREY_BRICK_IMAGE, 2, 0, 628, SCREEN_WIDTH, 0, 0)
    ],
    enemies=[
        Slime(200, SCREEN_HEIGHT - 72, 1, 150, 278)
    ],
    coins=[
        Coin(216, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 30),
        Coin(168, SCREEN_HEIGHT - 72, 0, 1, 0, 0, SCREEN_HEIGHT - 72, SCREEN_HEIGHT - 102),
        Coin(216, SCREEN_HEIGHT - 72, 0, 1, 0, 0, SCREEN_HEIGHT - 72, SCREEN_HEIGHT - 102),
        Coin(264, SCREEN_HEIGHT - 72, 0, 1, 0, 0, SCREEN_HEIGHT - 72, SCREEN_HEIGHT - 102),
        Coin(40, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 30),
        Coin(30, SCREEN_HEIGHT - 260, 0, 1, 0, 0, SCREEN_HEIGHT - 252, SCREEN_HEIGHT - 282)
    ],
    diamonds=[
        Diamond(768, SCREEN_HEIGHT - 340, 0, 1, 0, 0, SCREEN_HEIGHT - 332, SCREEN_HEIGHT - 372)
    ]
)

level_1 = Level(
    0, 0, 0, 0
)

        