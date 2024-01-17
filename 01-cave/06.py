import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))

FPSCLOCK = pygame.time.Clock()


def main():
    ship_y = 250
    velocity = 0
    ship_image = pygame.image.load("ship.png")

    while True:
        is_space_down = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                is_space_down = True

        velocity += -3 if is_space_down else 3
        ship_y += velocity

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
