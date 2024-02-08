import sys
from random import randint

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    game_over = False
    speed = 25
    rocks = []
    keymap = []
    ship = [0, 0]
    rock_image = pygame.image.load("rock.png")

    sysfont = pygame.font.SysFont(None, 72)
    message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (400, 400)

    while len(rocks) < 200:
        rocks.append({
            "pos": [randint(-1600, 1600),
                    randint(-1600, 1600),
                    randint(0, 4095)],
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

        if not game_over:

            if K_LEFT in keymap:
                ship[0] -= 30
            elif K_RIGHT in keymap:
                ship[0] += 30
            elif K_UP in keymap:
                ship[1] -= 30
            elif K_DOWN in keymap:
                ship[1] += 30

            for rock in rocks:
                rock["pos"][2] -= speed
                if rock["pos"][2] < 64:
                    if abs(rock["pos"][0] - ship[0]) < 50 and \
                            abs(rock["pos"][1] - ship[1]) < 50:
                        game_over = True
                    rock["pos"] = [randint(-1600, 1600),
                                   randint(-1600, 1600), 4095]

        SURFACE.fill((0, 0, 0))
        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - ship[0]) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - ship[1]) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        if game_over:
            SURFACE.blit(message_over, message_rect)

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()

