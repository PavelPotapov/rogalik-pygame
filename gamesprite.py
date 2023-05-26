import pygame
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,filename,x,y,w,h,a=0):
        self.image = pygame.transform.scale(pygame.image.load(filename), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = w
        self.height = h
        self.angle = a
    def draw(self,win):
        win.blit(self.image, (self.rect.x, self.rect.y))
