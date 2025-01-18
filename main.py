import pygame
import os
import sys
from math import(cos, sin,radians)

from setuptools.command.rotate import rotate

pygame.init()


WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
from load import *
clock = pygame.time.Clock()
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

    def update(self, *args, **kwargs):
        self.rotate()
        self.move()

    def rotate(self):
        self.deg_rotate -= 20
        self.image = pygame.transform.rotate(topor_image, self.deg_rotate)


    def move(self):
        self.deg += 3
        self.rect.centerx =150 * cos(radians(self.deg)) + player.rect.centerx
        self.rect.centery = 150 * sin(radians(self.deg)) + player.rect.centery


class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.key = pygame.key.get_pressed()
        self.speed = 5
        self.timer_anime = 0
        self.anime = False
        self.frame = 0
        self.pos_maps = [0,0]
        self.score = 0
        self.topor = 3
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
        if self.key[pygame.K_d]:
            self.dir = 'right'
            self.anime = True
            self.image = player_image[self.frame]
            self.rect.x += self.speed
            if self.rect.right > 1000:
                self.rect.right = 1000
        elif self.key[pygame.K_a]:
            self.image = pygame.transform.flip(player_image[self.frame], True, False)
            self.anime = True
            self.dir = 'left'
            self.rect.x -= self.speed
            if self.rect.left <200:
                self.rect.left = 200




    def update(self, *args, **kwargs):
        self.move()










def restart():
    global player_group, topor_group,player
    player_group = pygame.sprite.Group()
    topor_group = pygame.sprite.Group()
    player = Player(player_image,(150,100))
    player_group.add(player)
    player.add_topor()




def game_lvl():
    sc.fill('gray')
    player_group.update()
    player_group.draw(sc)
    topor_group.update()
    topor_group.draw(sc)
    pygame.display.update()





restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)


