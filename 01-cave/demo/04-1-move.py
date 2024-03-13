import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, KEYUP

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    ship_y = 250                                        ###
    move_y = 3                                          ###
    ship_image = pygame.image.load("ship.png")

    while True:

        '''InputEvent'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                move_y = -3
            elif event.type == KEYUP and event.key == K_SPACE:
                move_y = +3

        '''Update'''
        ship_y += move_y

        '''Rendering'''
        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, ship_y))   ###

        pygame.display.update()

        FPSCLOCK.tick(15)


main()

