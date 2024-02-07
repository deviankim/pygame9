import sys
from random import randint

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    rocks = []

    rock_image = pygame.image.load("rock.png")

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

        SURFACE.fill((0, 0, 0))

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - 0) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - 0) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()
