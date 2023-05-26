import pygame
from item import *
from gamesprite import *
from time import sleep

class Hero(GameSprite):
    def __init__(self,filename,x,y,w,h,a=0,sp=1):
        super().__init__(filename,x,y,w,h)
        self.speed = sp
        self.inventory = []
        self.showinv = True
    
    def drawinv(self,win):
        if self.showinv:
            y = 0
            for i in range(8):
                rect1 = pygame.Rect(650,y,50,50)
                pygame.draw.rect(win,(0,0,0),rect1,width=2)
                y += 50
            y = 0
            for i in self.inventory:
                if i.id == 1:
                    #itemdraw = GameSprite("items/dpotion.png", 652, y+2, 46,46)
                    i.rect.x = 652-20
                    i.rect.y = y+2
                    win.blit(i.image,(i.rect.x,i.rect.y))
                if i.id == 2:
                    #itemdraw = GameSprite("items/spotion.png", 652, y+2, 46,46)
                    i.rect.x = 652-20
                    i.rect.y = y+2
                    win.blit(i.image,(i.rect.x,i.rect.y))
                if i.id == 3:
                    #itemdraw = GameSprite("items/cycore.png", 652, y+2, 46,46)
                    i.rect.x = 652-20
                    i.rect.y = y+2
                    win.blit(i.image,(i.rect.x,i.rect.y))
                y += 50
    def collideWalls(self, walls):
        for wall in walls:
            if wall.rect.colliderect(self.rect):
                return wall
        return False
    def playeroutwall(self, wall):
       
        # if wall != False:
        #     if self.rect.y < wall.rect.y + wall.height and (keys[pygame.K_w] or (keys[pygame.K_w] and keys[pygame.K_a]) or (keys[pygame.K_w] and keys[pygame.K_d])):# снизу
        #         self.rect.y = wall.rect.y + wall.height + 1
        #         print('снизу')
        #         #sleep(1)
        #     elif self.rect.y + self.width > wall.rect.y and (keys[pygame.K_s] or (keys[pygame.K_s] and keys[pygame.K_a]) or (keys[pygame.K_s] and keys[pygame.K_d])): # сверху
        #         print('сверху')
        #         #sleep(1)
        #         self.rect.y = wall.rect.y - self.width - 1
        #     elif self.rect.x + self.width > wall.rect.x and (keys[pygame.K_d] or (keys[pygame.K_d] and keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_d])): # слева
        #         self.rect.x = wall.rect.x - self.width - 1
        #         print('слева')
        #         #sleep(1)
        #     elif self.rect.x < wall.rect.x + wall.width and (keys[pygame.K_d] or (keys[pygame.K_d] and keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_d])): #справа
        #         self.rect.x = wall.rect.x + wall.width + 1
        #         print('справа')
        #         #sleep(1)
        keys = pygame.key.get_pressed()
        if wall != False:
            if keys[pygame.K_w] and keys[pygame.K_a] or keys[pygame.K_w] and keys[pygame.K_d]:
                if self.rect.y < wall.rect.bottom and self.rect.x > wall.rect.left and self.rect.x < wall.rect.right:
                    print('снизу')
                    self.rect.y = wall.rect.y + wall.height + 1
                elif self.rect.y < wall.rect.bottom and self.rect.x + self.width > wall.rect.left and self.rect.x + self.width < wall.rect.right:
                    print('слева')
                    self.rect.x = wall.rect.x - self.width - 1
                elif self.rect.y < wall.rect.bottom and self.rect.x < wall.rect.right and self.rect.x > wall.rect.left:
                    print('справа')
                    self.rect.x = wall.rect.x + wall.width + 1
            elif keys[pygame.K_s] and keys[pygame.K_a] or keys[pygame.K_s] and keys[pygame.K_d]:
                if self.rect.y + self.height > wall.rect.top and self.rect.x > wall.rect.left and self.rect.x < wall.rect.right:
                    print('сверху')
                    self.rect.y = wall.rect.y - self.height - 1
                elif self.rect.y + self.height > wall.rect.top and self.rect.x + self.width > wall.rect.left and self.rect.x + self.width < wall.rect.right:
                    print('слева')
                    self.rect.x = wall.rect.x - self.width - 1
                elif self.rect.y + self.height > wall.rect.top and self.rect.x < wall.rect.right and self.rect.x > wall.rect.left:
                    print('справа')
                    self.rect.x = wall.rect.x + wall.width + 1
            elif keys[pygame.K_w]:
                if self.rect.y < wall.rect.bottom:
                    print('снизу')
                    self.rect.y = wall.rect.y + wall.height + 1
            elif keys[pygame.K_s]:
                if self.rect.y + self.height > wall.rect.top:
                    print('сверху')
                    self.rect.y = wall.rect.y - self.height - 1
            elif keys[pygame.K_a]:
                if self.rect.x < wall.rect.right:
                    print('справа')
                    self.rect.x = wall.rect.x + wall.width + 1
            elif keys[pygame.K_d]:
                if self.rect.x + self.width > wall.rect.x:
                    print('слева')
                    self.rect.x = wall.rect.x - self.width - 1

            
        


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
    def loot(self,chest):
        if chest.isLooted == False:
            for id in chest.items:
                if len(self.inventory)<8:
                    if id == 1:
                        item = DamagePotion("items/dpotion.png", 50, 69, 69, 46, 1) #тут будет предмет
                        self.inventory.append(item)
                    if id == 2:
                        item = ShieldPotion("items/spotion.png", 50, 69, 69, 46, 2) #тут будет предмет
                        self.inventory.append(item)
                    if id == 3:
                        item = CyberCore("items/cycore.png", 50, 69, 69, 46, 3) #тут будет предмет
                        self.inventory.append(item)
            chest.isLooted = True