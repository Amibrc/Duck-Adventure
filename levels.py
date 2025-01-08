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
    def __init__(self, objects, mobs, coins, diamonds):
        self.all_objects = objects + mobs + coins + diamonds
        self.objects = objects
        self.mobs = mobs
        self.coins = coins
        self.diamonds = diamonds
        
    
    def draw(self, surface):
        for obj in self.all_objects:
            obj.draw(surface)
    

    def update(self):
        for obj in self.objects:
            if obj.type == 'moved':
                obj.update()

        for mob in self.mobs:
            mob.update()
            if mob.death_animation_ended:
                self.mobs.remove(mob)
                self.all_objects.remove(mob)

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


class LevelManager():
    def __init__(self, levels):
        self.levels = levels
        self.current_level_index = 0
        self.current_level = self.levels[self.current_level_index]
        self.all_level_objects = self.current_level.all_objects
    

    def draw(self, surface):
        self.current_level.draw(surface)


    def update(self):
        self.current_level.update()

    
    def next_level(self):
        if self.current_level_index < len(self.levels) - 1:
            self.current_level_index += 1
            self.current_level = self.levels[self.current_level_index]
            self.all_level_objects = self.current_level.all_objects
    
    
    def check_diamond(self):
        if not self.current_level.diamonds:
            self.next_level()
            return True
        return False
    

    def check_mobs(self):
        if not self.current_level.mobs:
            self.next_level()
            return True
        return False


    def check_coins(self):
        if not self.current_level.coins:
            self.next_level()
            return True
        return False
    

    



SCREEN_WIDTH, SCREEN_HEIGHT = get_display_settings(True, True, False)

level_test = Level(
    objects=[
        StaticObject(0, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE),
        StaticObject(0, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE),
        StaticObject(182, SCREEN_HEIGHT - 170, GREY_BRICK_IMAGE), StaticObject(214, SCREEN_HEIGHT - 170, GREY_BRICK_IMAGE),
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
    mobs=[
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
    objects=[
        StaticObject(0, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE),
        StaticObject(0, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 220, GREY_BRICK_IMAGE)
    ],
    mobs=[
        Slime(200, SCREEN_HEIGHT, 1, 150, 278)
    ],
    coins=[

    ],
    diamonds=[
        Diamond(768, SCREEN_HEIGHT - 340, 0, 1, 0, 0, SCREEN_HEIGHT - 332, SCREEN_HEIGHT - 372)
    ]
)



level_manager = LevelManager((level_test, level_1))