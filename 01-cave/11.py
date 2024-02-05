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
    bang_image = pygame.image.load("bang.png")  # 우주선 폭발 효과 이미지

    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))
    game_over = False

    while True:
        is_space_down = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                is_space_down = True

        if not game_over:
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

            if holes[0].top > ship_y or \
                    holes[0].bottom < ship_y + 80:
                game_over = True

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        if game_over:  # 게임 오버일 때 우주선 폭발 이미지 그리기
            SURFACE.blit(bang_image, (0, ship_y - 40))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()