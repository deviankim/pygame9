""" saturn_voyager.py - Copyright 2016 Kenichiro Tanaka """
import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, \
    K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()

def main():
    """ 메인 루틴 """
    game_over = False
    score = 0
    speed = 25
    rocks = []
    keymap = []
    ship = [0, 0]
    scope_image = pygame.image.load("scope.png")
    rock_image = pygame.image.load("rock.png")

    scorefont = pygame.font.SysFont(None, 36)
    sysfont = pygame.font.SysFont(None, 72)
    message_over = sysfont.render("GAME OVER!!",\
                                        True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (400, 400)

    while len(rocks) < 200:
        rocks.append({
            "pos": [randint(-1600, 1600),
                    randint(-1600, 1600), randint(0, 4095)],
            "theta": randint(0, 360)
        })

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if not event.key in keymap:
                    keymap.append(event.key)
            elif event.type == KEYUP:
                keymap.remove(event.key)

        # 프레임별 처리
        if not game_over:
            score += 1
            if score % 10 == 0:
                speed += 1

            if K_LEFT in keymap:
                ship[0] -= 30
            elif K_RIGHT in keymap:
                ship[0] += 30
            elif K_UP in keymap:
                ship[1] -= 30
            elif K_DOWN in keymap:
                ship[1] += 30

            ship[0] = max(-800, min(800, ship[0]))
            ship[1] = max(-800, min(800, ship[1]))

            for rock in rocks:
                rock["pos"][2] -= speed
                if rock["pos"][2] < 64:
                    if abs(rock["pos"][0] - ship[0]) < 50 and \
                        abs(rock["pos"][1] - ship[1]) < 50:
                        game_over = True
                    rock["pos"] = [randint(-1600, 1600),
                                   randint(-1600, 1600), 4095]

        # 그리기
        SURFACE.fill((0, 0, 0))
        rocks = sorted(rocks, key=lambda x: x["pos"][2],
                       reverse=True)
        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - ship[0]) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - ship[1]) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image,
                                    rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        SURFACE.blit(scope_image, (0, 0))

        if game_over:
            SURFACE.blit(message_over, message_rect)
            pygame.mixer.music.stop()

        # 점수 나타내기
        score_str = str(score).zfill(6)
        score_image = scorefont.render(score_str, True,
                                       (0, 255, 0))
        SURFACE.blit(score_image, (700, 50))

        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()
