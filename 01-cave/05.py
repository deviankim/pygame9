import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))

FPSCLOCK = pygame.time.Clock()


def main():
    ship_y = 0
    velocity = 0
    ship_image = pygame.image.load("ship.png")

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        velocity += 3
        ship_y += velocity

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
