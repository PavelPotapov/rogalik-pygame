import pygame
import math
from settings import FPS
from gamesprite import *
from random import *

class Enemy(GameSprite):
    def __init__(self, filename, x, y, w, h, angle=0,speed=1):
        super().__init__(filename, x, y, w, h, angle)
        self.speed = random() * randint(1,2) + 1
        self.time = 5
        self.stepx = 0
        self.stepy = 0
    def moveTowards(self,obj):
        #расстояние между врагом и героем
        #s = math.sqrt((self.rect.x - obj.rect.x)**2+(self.rect.y - obj.rect.y)**2)
        #self.time = 5*s/922

        self.stepx = abs((self.rect.x - obj.rect.x) / FPS)
        self.stepy = abs((self.rect.y - obj.rect.y) / FPS)

       
        if self.stepx < 1:
            self.stepx = 1

        if self.stepy < 1:
            self.stepy = 1
        
        if self.rect.x > obj.rect.x:
            self.rect.x -= self.stepx
            print('Двигаюсь влево')
        else:
            self.rect.x += self.stepx
            print('Двигаюсь вправо', self.stepx)

        if self.rect.y > obj.rect.y:
            self.rect.y -= self.stepy
            print('Двигаюсь вниз')
        else:
            self.rect.y += self.stepy
            print('Двигаюсь вверх', self.stepy)