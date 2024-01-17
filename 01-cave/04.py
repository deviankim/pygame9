import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    ship_image = pygame.image.load("ship.png")

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, 0))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
