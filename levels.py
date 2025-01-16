from objects import *
from mobs import *
from tools import get_display_settings
from config.images import (
    RED_BRICK_IMAGE,
    GREY_BRICK_IMAGE,
    STONE_IMAGE
)

class Level():
    def __init__(self, objects, mobs, coins, diamonds, level_size, start_pos, win_condition):
        self.all_objects = objects + mobs + coins + diamonds
        self.objects = objects
        self.mobs = mobs
        self.coins = coins
        self.diamonds = diamonds
        self.level_width, self.level_height = level_size
        self.start_pos = start_pos
        self.win_condition = win_condition


        self.copy_objects = [obj.copy() if obj.type == "moved" else obj for obj in objects]
        self.copy_mobs = [mob.copy() for mob in mobs]
        self.copy_coins = [coin.copy() for coin in coins]
        self.copy_diamonds = [diamond.copy() for diamond in diamonds]
        self.copy_all_objects = self.copy_objects + self.copy_mobs + self.copy_coins + self.copy_diamonds

    
    def draw(self, surface, camera):
        for obj in self.all_objects:
            if obj.type == "static" or obj.type == "moved":
                surface.blit(obj.object_image, camera.apply(obj.object_rect))
            elif obj.type == "entity":
                surface.blit(obj.current_animation, camera.apply(obj.object_rect))
            else:
                surface.blit(obj.current_frame_mob, camera.apply(obj.object_rect))
    

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
    

    def restart(self):
        self.objects = [obj.copy() if obj.type == "moved" else obj for obj in self.copy_objects]
        self.mobs = [mob.copy() for mob in self.copy_mobs]
        self.coins = [coin.copy() for coin in self.copy_coins]
        self.diamonds = [diamond.copy() for diamond in self.copy_diamonds]
        self.all_objects = self.objects + self.mobs + self.coins + self.diamonds
    

    def get_level_size(self):
        return self.level_width, self.level_height


class LevelManager():
    def __init__(self, levels):
        self.levels = levels
        self.current_level_index = 0
        self.current_level = self.levels[self.current_level_index]
        self.all_level_objects = self.current_level.all_objects
    

    def draw(self, surface, camera):
        self.current_level.draw(surface, camera)


    def update(self):
        self.current_level.update()

    
    def next_level(self):
        if self.current_level_index < len(self.levels) - 1:
            self.current_level_index += 1
            self.current_level = self.levels[self.current_level_index]
            self.all_level_objects = self.current_level.all_objects
    

    def restart_level(self):
        self.current_level.restart()
        self.all_level_objects = self.current_level.all_objects
    

    def check_win_condition(self):
        if self.current_level.win_condition == "diamonds":
            return self.check_diamond()
        elif self.current_level.win_condition == "mobs":
            return self.check_mobs()
        elif self.current_level.win_condition == "coins":
            return self.check_coins()
        return False

    
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
        StaticObject(768, SCREEN_HEIGHT - 300, GREY_BRICK_IMAGE), StaticObject(736, SCREEN_HEIGHT - 300, GREY_BRICK_IMAGE), StaticObject(704, SCREEN_HEIGHT - 300, GREY_BRICK_IMAGE), StaticObject(672, SCREEN_HEIGHT - 300, GREY_BRICK_IMAGE),
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
    ],
    level_size=(1500, 600),
    start_pos=(80, SCREEN_HEIGHT),
    win_condition=None
)


level_1 = Level(
    objects=[
        StaticObject(250, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE), StaticObject(282, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE),
        StaticObject(314, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE), StaticObject(346, SCREEN_HEIGHT - 70, RED_BRICK_IMAGE),

        StaticObject(0, SCREEN_HEIGHT - 140, RED_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 140, RED_BRICK_IMAGE),
        StaticObject(64, SCREEN_HEIGHT - 140, RED_BRICK_IMAGE),

        StaticObject(768, SCREEN_HEIGHT, RED_BRICK_IMAGE),
        StaticObject(800, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(800, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(832, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(832, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(864, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(864, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(896, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(896, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(928, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(928, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(960, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(960, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(992, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(992, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1024, SCREEN_HEIGHT, RED_BRICK_IMAGE),

        StaticObject(1184, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE), StaticObject(1216, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),
        StaticObject(1248, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(1408, SCREEN_HEIGHT, RED_BRICK_IMAGE),
        StaticObject(1440, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(1440, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1472, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(1472, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1504, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(1504, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1536, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(1536, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1568, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(1568, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1600, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(1600, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1632, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(1632, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(1664, SCREEN_HEIGHT, RED_BRICK_IMAGE),

        MovedObject(2000, SCREEN_HEIGHT, STONE_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 128),
        MovedObject(2032, SCREEN_HEIGHT, STONE_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 128),

        StaticObject(2064, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2064, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2064, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2064, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2096, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2096, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2096, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2096, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2128, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2128, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2128, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2128, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2160, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2160, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2160, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2160, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2192, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2192, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2192, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2192, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2224, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2224, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2224, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2224, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),
        
        StaticObject(2256, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2256, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2256, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2256, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2288, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2288, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2288, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2288, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2320, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2320, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2320, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2320, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2352, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2352, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2352, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2352, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE),

        StaticObject(2384, SCREEN_HEIGHT, RED_BRICK_IMAGE), StaticObject(2384, SCREEN_HEIGHT - 32, RED_BRICK_IMAGE),
        StaticObject(2384, SCREEN_HEIGHT - 64, RED_BRICK_IMAGE), StaticObject(2384, SCREEN_HEIGHT - 96, RED_BRICK_IMAGE)
    ],
    mobs=[
        RoyalScarab(250, SCREEN_HEIGHT - 102, 1, 250, 378),
        Slime(768, SCREEN_HEIGHT, -1, 500, 768),
        GiantRoyalScarab(1024, SCREEN_HEIGHT, 3, 1056, 1408),
        RoyalScarab(1696, SCREEN_HEIGHT, 2, 1696, 2000),
        Slime(2064, SCREEN_HEIGHT - 128, 1, 2064, 2400)
    ],
    coins=[
        Coin(266, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),
        Coin(314, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),
        Coin(362, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),

        Coin(266, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 32),
        Coin(314, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 32),
        Coin(362, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 32),

        Coin(848, SCREEN_HEIGHT - 64, 0, 1, 0, 0, SCREEN_HEIGHT - 64, SCREEN_HEIGHT - 96),
        Coin(912, SCREEN_HEIGHT - 64, 0, 1, 0, 0, SCREEN_HEIGHT - 64, SCREEN_HEIGHT - 96),
        Coin(976, SCREEN_HEIGHT - 64, 0, 1, 0, 0, SCREEN_HEIGHT - 64, SCREEN_HEIGHT - 96),

        Coin(1232, SCREEN_HEIGHT - 96, 0, 1, 0, 0, SCREEN_HEIGHT - 128, SCREEN_HEIGHT - 160),

        Coin(1488, SCREEN_HEIGHT - 64, 0, 1, 0, 0, SCREEN_HEIGHT -64, SCREEN_HEIGHT - 96),
        Coin(1552, SCREEN_HEIGHT - 64, 0, 1, 0, 0, SCREEN_HEIGHT -64, SCREEN_HEIGHT - 96),
        Coin(1616, SCREEN_HEIGHT - 64, 0, 1, 0, 0, SCREEN_HEIGHT - 64, SCREEN_HEIGHT - 96)
    ],
    diamonds=[
        Diamond(48, SCREEN_HEIGHT - 172, 0, 1, 0, 0, SCREEN_HEIGHT - 172, SCREEN_HEIGHT - 212),
        Diamond(1232, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 40),
        Diamond(2384, SCREEN_HEIGHT - 128, 0, 1, 0, 0, SCREEN_HEIGHT - 128, SCREEN_HEIGHT - 168)
    ],
    level_size=(2400, SCREEN_HEIGHT),
    start_pos=(80, SCREEN_HEIGHT),
    win_condition="diamonds"
)


level_2 = Level(
    objects=[
        StaticObject(0, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(32, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(64, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(96, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(128, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(160, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(192, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(224, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(256, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(288, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(320, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(352, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(384, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(416, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(448, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(480, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),

        MovedObject(512, SCREEN_HEIGHT - 70, STONE_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 102),
        MovedObject(544, SCREEN_HEIGHT - 70, STONE_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 102),

        StaticObject(208, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE), StaticObject(240, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE),
        StaticObject(272, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE), StaticObject(304, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE),

        MovedObject(960, SCREEN_HEIGHT - 70, STONE_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 102),
        MovedObject(992, SCREEN_HEIGHT - 70, STONE_IMAGE, 0, 2, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 102),

        StaticObject(1024, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1056, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(1088, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1120, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(1152, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1184, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(1216, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1248, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(1280, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1312, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(1344, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1376, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(1408, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1440, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),
        StaticObject(1472, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE), StaticObject(1504, SCREEN_HEIGHT - 70, GREY_BRICK_IMAGE),

        StaticObject(1024, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1056, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),
        StaticObject(1088, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1120, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),
        StaticObject(1152, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1184, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),
        StaticObject(1216, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1248, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),
        StaticObject(1280, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1312, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),
        StaticObject(1344, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1376, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),
        StaticObject(1408, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1440, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),
        StaticObject(1472, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE), StaticObject(1504, SCREEN_HEIGHT - 38, GREY_BRICK_IMAGE),

        StaticObject(1024, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1056, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),
        StaticObject(1088, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1120, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),
        StaticObject(1152, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1184, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),
        StaticObject(1216, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1248, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),
        StaticObject(1280, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1312, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),
        StaticObject(1344, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1376, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),
        StaticObject(1408, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1440, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),
        StaticObject(1472, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE), StaticObject(1504, SCREEN_HEIGHT - 6, GREY_BRICK_IMAGE),

        StaticObject(1024, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1056, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),
        StaticObject(1088, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1120, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),
        StaticObject(1152, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1184, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),
        StaticObject(1216, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1248, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),
        StaticObject(1280, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1312, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),
        StaticObject(1344, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1376, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),
        StaticObject(1408, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1440, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),
        StaticObject(1472, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE), StaticObject(1504, SCREEN_HEIGHT + 26, GREY_BRICK_IMAGE),

        StaticObject(1232, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE), StaticObject(1264, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE),
        StaticObject(1296, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE), StaticObject(1328, SCREEN_HEIGHT - 172, GREY_BRICK_IMAGE),

        


        

    ],
    mobs=[
        RoyalScarab(208, SCREEN_HEIGHT - 204, 1, 208, 336),
        Bee(502, SCREEN_HEIGHT - 42, -4, 0, 502),
        Slime(960, SCREEN_HEIGHT, -1, 576, 960)
    ],
    coins=[
        Coin(224, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),
        Coin(272, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),
        Coin(320, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),

        Coin(224, SCREEN_HEIGHT - 204, 0, 1, 0, 0, SCREEN_HEIGHT - 204, SCREEN_HEIGHT - 236),
        Coin(272, SCREEN_HEIGHT - 204, 0, 1, 0, 0, SCREEN_HEIGHT - 204, SCREEN_HEIGHT - 236),
        Coin(320, SCREEN_HEIGHT - 204, 0, 1, 0, 0, SCREEN_HEIGHT - 204, SCREEN_HEIGHT - 236),

        Coin(1248, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),
        Coin(1296, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),
        Coin(1344, SCREEN_HEIGHT - 102, 0, 1, 0, 0, SCREEN_HEIGHT - 102, SCREEN_HEIGHT - 134),

        Coin(1248, SCREEN_HEIGHT - 204, 0, 1, 0, 0, SCREEN_HEIGHT - 204, SCREEN_HEIGHT - 236),
        Coin(1296, SCREEN_HEIGHT - 204, 0, 1, 0, 0, SCREEN_HEIGHT - 204, SCREEN_HEIGHT - 236),
        Coin(1344, SCREEN_HEIGHT - 204, 0, 1, 0, 0, SCREEN_HEIGHT - 204, SCREEN_HEIGHT - 236),

    ],
    diamonds=[
        Diamond(16, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 40),
        Diamond(2000, SCREEN_HEIGHT, 0, 1, 0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT - 40)

    ],
    level_size=(2000, SCREEN_HEIGHT),
    start_pos=(80, SCREEN_HEIGHT - 102),
    win_condition="diamonds"
)



level_manager = LevelManager((level_2, level_test))