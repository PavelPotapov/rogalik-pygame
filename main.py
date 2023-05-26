import pygame
from hero import Hero
from enemy import Enemy
from settings import *
from room import *
from text import *

window = pygame.display.set_mode(WIN_SIZE)
clock = pygame.time.Clock()
run = True
finish = False 
timer_finih = 500


hero = Hero("plus.png",200,100,40,40)
enemy = Enemy("del.png",500,500,40,40)
enemy2 = Enemy("del.png",0,500,40,40)
room1 = Room(100,100)
room2 = Room(300,100)
room3 = Room(100,300)
room4 = Room(300,300)
rooms = [room1,room2,room3,room4]
enemies = [enemy,enemy2]
while run:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
               hero.showinv = not hero.showinv 
    for room in rooms:
        room.draw(window)

    for enemy in enemies:
        enemy.draw(window)
        enemy.moveTowards(hero)
        if enemy.rect.colliderect(hero.rect):
            finish = True

    #dsalose
    if finish:
        lose_text = font.render('YOU LOOOSE AFTER: ' + str(timer_finih) + 'ms', True, (255,0,0))
        window.blit(lose_text, (250, 250))
        timer_finih -= 1
        if timer_finih <=0:
            run = False

    hero.draw(window)
    hero.move()
    hero.drawinv(window)
    for room in rooms:
        for chest in room.chests:
            if chest.rect.colliderect(hero.rect):
                hero.loot(chest)
        for spawner in room.spawners:
            spawner.draw(window)
            #enemy = spawner.spawn() 
            #if enemy != False:
            #    enemies.append(enemy)
        hero.playeroutwall(hero.collideWalls(room.walls))

    
    clock.tick(FPS)
    pygame.display.update()