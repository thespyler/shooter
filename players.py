import pygame
from pygame.locals import *
from random import randrange
from settings import * 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship#pygame.Surface((50, 40))
        # self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.rect.center = (height // 20, width - 40)
        self.speed = 0
        self.speedY = 0
    def update(self):
        keys = pygame.key.get_pressed()
        keylift = not pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.speed = -8

        elif keys[K_RIGHT]:
            self.speed = 8

        elif keys[K_UP]:
            self.speedY = -8

        elif keys[K_DOWN]:
            self.speedY = 8

        if keylift:
            self.speed = 0
            self.speedY = 0
        self.rect.x += self.speed
        self.rect.y += self.speedY

        if self.rect.left > height:
            self.rect.left = 0

        if self.rect.right <= 0:
            self.rect.right = height

        if self.rect.top <= 0:
            self.rect.bottom = width

        if self.rect.bottom >= width:
            self.rect.top = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, 400)
        self.rect.y = width
        self.speedx = randrange(-1, 1)
        self.speedy = randrange(1, 9)

    def update(self):
        if self.rect.bottom > width or self.rect.left < 0 or self.rect.right > height:
            self.rect.x = randrange(100, height)
            self.rect.y = randrange(-10, 0)
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser
        # self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
