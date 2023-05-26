import pygame
from item import *
from enemy import *
class Wall:
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)
        self.width = w
        self.height = h
class Room:
    def __init__(self,x,y) -> None:
        self.walls = []
        self.chests = []
        self.spawners = []
        self.traps = []
        self.x = x
        self.y = y
        self.width = 200
        self.height = 200
        self.wallgen()
        self.chestgen()
        self.spawngen()
    def wallgen(self):
        w1 = Wall(self.x,self.y,75,20)
        w2 = Wall(self.x,self.y+20,20,55)
        w3 = Wall(self.x,self.y+125,20,55)
        w4 = Wall(self.x,self.y+180,75,20)
        w5 = Wall(self.x+125,self.y,75,20)
        w6 = Wall(self.x+180,self.y+20,20,55)
        w7 = Wall(self.x+180,self.y+125,20,55)
        w8 = Wall(self.x+125,self.y+180,75,20)
        self.walls.append(w1)
        self.walls.append(w2)
        self.walls.append(w3)
        self.walls.append(w4)
        self.walls.append(w5)
        self.walls.append(w6)
        self.walls.append(w7)
        self.walls.append(w8)
    def spawngen(self):
        spawner = Spawner("spawner.png", self.x + 100, self.y + 100, 60,60)
        self.spawners.append(spawner)
    def chestgen(self):
        #функция, которая генерирует item внутри chesta, ну и создает сам сундук
        chest = Chest('chest.png', self.x, self.y, 90,90)
        self.chests.append(chest)
    def trapgen(self):
        pass

    def draw_walls(self,win):
        for wall in self.walls:
            pygame.draw.rect(win,(0,0,0),wall)

    def draw_chest(self,win):
        for chest in self.chests:
            win.blit(chest.image,(chest.rect.x,chest.rect.y))
    def draw(self,win):
        self.draw_walls(win)
        self.draw_chest(win)

class Spawner(GameSprite):
    def __init__(self, filename, x, y, w, h, a=0):
        super().__init__(filename, x, y, w, h, a)
        self.count = 0
    def spawn(self):
        if self.count == 100:
            enemy = Enemy("del.png",self.rect.x,self.rect.y,40,40)
            self.count = 0
            return enemy
        else:
            self.count += 1
            return False

class Trap(GameSprite):
    def __init__(self, filename, x, y, w, h, activate, d, t, active_img, a=0):
        super().__init__(filename, x, y, w, h, a)
        self.activate = activate #активна ли ловушка
        self.delay = d #задержка перед активацией
        self.time = t #время активности ловушки
        self.active_img = active_img #картинка сработавшей ловушки
        self.buff_image = ""
        self.count = 0 #счетчик перед активацией
        self.count1 = 0
    def activate_trap(self):
        self.count += 1
        if self.count >= self.delay:
            self.activate = True if randint(1,3) == 1 else False
            if self.activate == False:
                self.count = 0
    def activecheck(self):
        if self.activate:
            self.count1 += 1
            if self.count1 >= self.time:
                self.activate = False
                self.count = 0
        
            
