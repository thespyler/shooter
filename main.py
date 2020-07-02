import pygame
from pygame.locals import *
from random import randrange
from settings import *
from players import *

display = pygame.display.set_mode((height, width))
pygame.display.set_caption('game')


def main():
    # /global SCORE
    pygame.init()
    player = Player()
    mob = Mob()
    bullet = Bullet(player.rect.x, player.rect.y)
    mobs = pygame.sprite.Group()
    mobs.add(mob)
    players = pygame.sprite.Group()
    players.add(player)
    bullets = pygame.sprite.Group()
    bullets.add(bullet)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bullet)
    all_sprites.add(player)
    all_sprites.add(mob)
    SCORE = 0
    for i in range(10):
        m = Mob()
        mobs.add(m)
        all_sprites.add(m)

    while game_on:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    for b in range(5):
                        b = Bullet(player.rect.x + 50, player.rect.y - 50)
                        bullets.add(b)
                        all_sprites.add(b)
                   #pygame.mixer.music.play(1)

            if event.type == KEYUP:
                player.speed = 0
                player.speedY = 0
        # display.blit(bg, [0, 0])
        display.fill(BLACK)
        hits = pygame.sprite.groupcollide(players, mobs, False, False)
        bullethit = pygame.sprite.groupcollide(bullets, mobs, True, True)
        if bullethit:
            m = Mob()
            mobs.add(m)
            all_sprites.add(m)
            SCORE += 5
        if hits:
            gameover(SCORE)
            running = False
            # return
        ScoreFont("SCORE = " + str(SCORE), GREEN, display)
        all_sprites.update()
        all_sprites.draw(display)
        pygame.display.update()
        pygame.time.Clock().tick(60)


def gameover(SCORE):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_c:
                    # game_on = True
                    main()

        # print('hits')
        display.fill(WHITE)
        Fonter("You Died!!", RED, display)
        ScoreFont("SCORE = " + str(SCORE), GREEN, display)

        pygame.display.update()


if __name__ == '__main__':
    main()
