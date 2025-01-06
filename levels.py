class Level():
    def __init__(self, objects, enemies, coins, diamonds):
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
            obj.update()

        for enemy in self.enemies:
            enemy.update()

        for coin in self.coins:
            coin.update()
            if coin.collected:
                self.coins.remove(coin)
            
        
        for diamond in self.diamonds:
            diamond.update()
            if diamond.collected:
                self.diamonds.remove(diamond)

        