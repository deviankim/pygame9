import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    ship_y = 0  # 우주선의 좌표 초기값
    velocity = 0  # 우주선의 가속도 초기값
    ship_image = pygame.image.load("ship.png")

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        velocity += 3  # 중력 가속도를 3씩 증가
        ship_y += velocity  # 우주선 y 좌표에 중력 가속도를 더해서 아래로 떨어지게 한다.

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, ship_y))  # ship_y 를 사용하여 y 좌표 지정

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
