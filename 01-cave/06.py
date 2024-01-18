import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect  # Rect 클래스 불러오기

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))

FPSCLOCK = pygame.time.Clock()


def main():
    walls = 80  # 벽의 가로 길이 80으로 지정 (80 * 10 = 800)
    ship_y = 250
    velocity = 0
    ship_image = pygame.image.load("ship.png")

    holes = []  # 구멍 리스트 준비
    for xpos in range(walls):  # 변수 xpos 는 0 부터 79 까지 반복 할당 된다.
        holes.append(Rect(xpos * 10, 100, 10, 400))  # 구멍 리스트에 Rect 추가: 오른쪽으로 10씩 이동하면서 배치됨

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

        for hole in holes:  # 구멍 리스트에서 하나씩 꺼내서 아래 블럭 실행
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)  # 구멍을 검은색 (0, 0, 0) 으로 그려 준다.

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
