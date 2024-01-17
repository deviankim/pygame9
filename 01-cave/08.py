import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    walls = 80
    ship_y = 250
    velocity = 0
    slope = randint(1, 6)  # 경사도를 [1,2,3,4,5,6] 중에 하나를 랜덤하게 선택
    ship_image = pygame.image.load("ship.png")

    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))

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

        edge = holes[-1].copy()
        test = edge.move(0, slope)
        if test.top <= 0 or test.bottom >= 600:
            slope = randint(1, 6) * (-1 if slope > 0 else 1)  # 랜덤 경사도에 (+/-) 부호 전환
            # TODO: (-1 if slope > 0 else 1) 을 더 간단하게 변경

        edge.move_ip(10, slope)
        holes.append(edge)

        del holes[0]
        holes = [x.move(-10, 0) for x in holes]

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
