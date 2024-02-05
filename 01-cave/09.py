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
    slope = randint(1, 6)
    ship_image = pygame.image.load("ship.png")

    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))
    game_over = False  # 게임오버 변수 선언

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
            slope = randint(1, 6) * (-1 if slope > 0 else 1)

        edge.move_ip(10, slope)
        holes.append(edge)

        del holes[0]
        holes = [x.move(-10, 0) for x in holes]

        # 우주선이 첫번째 구멍을 벗어나는지 검사
        if holes[0].top > ship_y or \
                holes[0].bottom < ship_y + 80:
            game_over = True  # 게임오버로 판정

        print('game_over:', game_over)  # 게임오버인지 확인

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()