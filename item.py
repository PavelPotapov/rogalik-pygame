import pygame
from random import *
from gamesprite import *

items_description = {
    1: 'Зелье урона. Это зелье можно бросить (выстрелить) во врага и он умерт', 
    2: 'Зелье щита, 10 секунд игрок неуязвим.', 
    3: 'Кибер ядро. Выбрасывает линию пустоты вперед, но если изпользовать слишком много изчезает из инвентаря'
}

class Item(GameSprite):
    def __init__(self,filename1,x,y,w,h,id,a=0):
        super().__init__(filename1,x,y,w,h,a)
        self.description = items_description[id]

class DamagePotion(Item):
    #функция, которая запускает зелье в какую-то сторону
    id = 1
    def move(self):
        pass
class ShieldPotion(Item):
    #функция, которая отслеживает жизнь щита
    id = 2
    def live(self):
        pass
class CyberCore(Item):
    id = 3
    def laser(self):
        pass
class Chest(GameSprite):
    #класс сундука
    def __init__(self, filename, x, y, w, h, a=0):
        super().__init__(filename, x, y, w, h, a)
        self.items = []
        self.isLooted = False
        self.itemgen()

    def itemgen(self):
        item_count = randint(1,2)
        for i in range(item_count):
            genitem = randint(1,3)
            self.items.append(genitem)
