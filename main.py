from random import choice

import pygame
import os
import sys
from math import(cos, sin,radians)

from pygame.camera import Camera
from setuptools.command.rotate import rotate

pygame.init()


WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
from load import *
clock = pygame.time.Clock()
class Camera():
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
class Topor(pygame.sprite.Sprite):
    def __init__(self,image,pos,start_deg):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.deg_rotate = 0
        self.deg = start_deg
        self.timer_attack = 0
        self.topor = 1

    def update(self, *args, **kwargs):
        self.rotate()
        self.move()

    def rotate(self):
        self.deg_rotate -= 20
        self.image = pygame.transform.rotate(topor_image, self.deg_rotate)


    def move(self):
        self.deg += 1
        self.rect.centerx =150 * cos(radians(self.deg)) + player.rect.centerx
        self.rect.centery = 150 * sin(radians(self.deg)) + player.rect.centery

    def collide(self):
        if pygame.spritecollide(self,spaider_group, False):
            self.topor += 1



class Stone(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir == 'left':
                player.rect.left = self.rect.right
            elif player.dir == 'right':
                player.rect.right = self.rect.left
            elif player.dir =='bottom':
                player.rect.bottom = self.rect.top
            elif player.dir =='top':
                player.rect.top = self.rect.bottom


class Spaider(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speedy = 1
        self.speedx =1



    def update(self):
        self.move()
        self.collide()
    def move(self):


        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def collide(self):
        if pygame.sprite.spritecollide(self,stone_group, False):
            self.speedx *= -1
            self.speedy *= -1
        if pygame.sprite.spritecollide(self,topor_group, False):
            self.kill()








# class Bonus(pygame.sprite.Sprite,Camera):
#     def __init__(self,image,pos):










class Water(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir == 'left':
                player.rect.left = self.rect.right
            elif player.dir == 'right':
                player.rect.right = self.rect.left
            elif player.dir =='bottom':
                player.rect.bottom = self.rect.top
            elif player.dir =='top':
                player.rect.top = self.rect.bottom




class Spawner(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.timer_spawn = 1


    def update(self):
        self.spawn()
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir == 'left':
                player.rect.left = self.rect.right
            elif player.dir == 'right':
                player.rect.right = self.rect.left
            elif player.dir =='bottom':
                player.rect.bottom = self.rect.top
            elif player.dir =='top':
                player.rect.top = self.rect.bottom

    def spawn(self):
        if 0< self.rect.centerx <1200 and 0 < self.rect.centery< 800:
            self.timer_spawn += 1
            if self.timer_spawn / FPS > 1:
                spaider = Spaider(spaider_image, self.rect.center)
                spaider_group.add(spaider)
                camera_group.add(spaider)
                self.timer_spawn = 0









class SuperGroup(pygame.sprite.Group):
    def camera_update(self,stepx, stepy):
        for sprite in self.sprites():
            sprite.camera_move(stepx,stepy)


class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.key = pygame.key.get_pressed()
        self.speed = 7
        self.timer_anime = 0
        self.anime = False
        self.frame = 0
        self.pos_maps = [0,0]
        self.score = 0
        self.topor = 5
        self.key = pygame.key.get_pressed()
        self.dir = 'right'
        self.camera = False






    def add_topor(self):
        global topor_group
        topor_group = pygame.sprite.Group()
        for i in range(self.topor):
            topor = Topor(topor_image,(self.rect.centerx + 70, self.rect.centery+70), (360 // self.topor * i))
            topor_group.add(topor)

    def move(self):
        # if self.key[pygame.K_d]:
        #    self.dir = 'right'
        #    self.anime = True
        #    self.image = player_image[self.frame]
        #    self.rect.x += self.speed
        #    if self.rect.right > 1000:
        #        self.rect.right = 1000
        #
        # elif self.key[pygame.K_a]:
        #    self.image = pygame.transform.flip(player_image[self.frame], True, False)
        #    self.anime = True
        #    self.dir = 'left'
        #    self.rect.x -= self.speed
        #    if self.rect.left < 200:
        #        self.rect.left = 200
        #        camera_group.update(self.speed)
        # elif self.key[pygame.K_w]:
        #    self.image = pygame.transform.flip(player_image[self.frame], True, False)
        #    self.anime = True
        #    self.dir = 'top'
        #    self.rect.y -= self.speed
        #    if self.rect.left < 200:
        #        self.rect.left = 500
        #        camera_group.update(self.speed)
        # elif self.key[pygame.K_s]:
        #    self.image = pygame.transform.flip(player_image[self.frame], True, False)
        #    self.anime = True
        #    self.dir = 'bottom'
        #    self.rect.y += self.speed
        #    if self.rect.right > 200:
        #        self.rect.right = 500
        #        camera_group.update(self.speed)
#

        if self.key[pygame.K_a]:
            self.image = player_image_1[self.frame]
            self.rect.x -= self.speed
            self.dir = 'left'
            if self.rect.left < 300 and self.pos_maps[0] < 0:
                self.pos_maps[0] += self.speed
                camera_group.camera_update(self.speed, 0)
                self.rect.left = 300
        elif self.key[pygame.K_d]:
            self.image = player_image_2[self.frame]
            self.rect.x += self.speed
            self.dir='right'
            if self.rect.right > 900 and self.pos_maps[0] > - 6800:
                self.pos_maps[0] -= self.speed
                camera_group.camera_update(-self.speed, 0)
                self.rect.right = 900
        elif self.key[pygame.K_s]:
            self.image = pygame.transform.flip(player_image[self.frame], True, False)
            self.dir = 'bottom'
            self.rect.y += self.speed
            if self.rect.bottom > 600 and self.pos_maps[1] > - 7200:
                self.pos_maps[1] -= self.speed
                camera_group.camera_update(0, -self.speed)
                self.rect.bottom = 600
        elif self.key[pygame.K_w]:
            self.image = player_image_3[self.frame]
            self.dir = 'top'
            self.rect.y -= self.speed
            if self.rect.top < 300 and self.pos_maps[1] < 0:
                self.pos_maps[1] += self.speed
                camera_group.camera_update(0, self.speed)
                self.rect.bottom = 300






    def update(self):
        self.key = pygame.key.get_pressed()
        self.move()








def drawMaps(nameFile):
    maps = []
    source = '' + str(nameFile)
    with open(source, 'r') as file:
        for i in range(0, 100):
            maps.append(file.readline().replace('\n', '').split(',')[0:-1])

    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == '1':
                stone = Stone(stone_image, pos)
                stone_group.add(stone)
                camera_group.add(stone)
            elif maps[i][j] == '3':
                water = Water(water_image, pos)
                water_group.add(water)
                camera_group.add(water)
            elif maps[i][j] == '2':
                spawner = Spawner(spawner_image, pos)
                spawner_group.add(spawner)
                camera_group.add(spawner)



def restart():
    global player_group, topor_group,player,stone_group,water_group,spawner_group,camera_group,spaider_group
    player_group = pygame.sprite.Group()
    spaider_group = pygame.sprite.Group()
    camera_group = SuperGroup()
    water_group = pygame.sprite.Group()
    spawner_group = pygame.sprite.Group()
    stone_group = pygame.sprite.Group()
    topor_group = pygame.sprite.Group()
    player = Player(player_image,(150,100))
    player_group.add(player)
    player.add_topor()




def game_lvl():
    sc.fill('gray')
    player_group.update()
    player_group.draw(sc)
    water_group.update()
    water_group.draw(sc)
    spawner_group.update()
    spawner_group.draw(sc)
    spaider_group.update()
    spaider_group.draw(sc)
    topor_group.update()
    stone_group.update()
    stone_group.draw(sc)
    topor_group.draw(sc)
    pygame.display.update()





restart()
drawMaps('rpgmap.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)


