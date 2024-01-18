import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    ship_image = pygame.image.load("ship.png")  # 우주선 이미지를 로딩

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, 0))  # 우주선 이미지를 화면 데이터의 (x,y)에 그리기

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
