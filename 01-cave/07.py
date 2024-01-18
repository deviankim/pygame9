import sys
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
    slope = 6  # 경사값 6으로 초기화
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

        edge = holes[-1].copy()  # 배열의 가장 끝(-1) 에 있는 구멍의 복사본 생성
        test = edge.move(0, slope)  # 구멍이 벽에 닿았는지 확인하기 위한 test 변수
        if test.top <= 0 or test.bottom >= 600:  # 벽에 닿았는지 조건 검사
            slope *= -1  # 경사에 -1 을 곱해 주어 반대 방향으로 전환

        edge.move_ip(10, slope)  # 가장자리 구멍을 경사값 만큼 y 좌표를 이동
        holes.append(edge)  # 가장자리를 구멍 리스트에 추가

        del holes[0]  # 맨 처음 구멍을 제거
        holes = [x.move(-10, 0) for x in holes]  # 구멍을 좌측으로 -10씩 이동 (스크롤 효과)

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()
