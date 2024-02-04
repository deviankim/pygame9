import sys
import pygame
from pygame.locals import QUIT

WIDTH = 20          # 가로 칸수
HEIGHT = 15         # 세로 칸수
SIZE = 50           # 각 칸의 크기

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])    # 전체 화면 크기
FPSCLOCK = pygame.time.Clock()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        # 세로 줄 긋기
        for index in range(0, WIDTH * SIZE, SIZE):  #
            pygame.draw.line(SURFACE, (96, 96, 96),  #
                             (index, 0), (index, HEIGHT * SIZE))  #
        # 가로 줄 긋기
        for index in range(0, HEIGHT * SIZE, SIZE):  #
            pygame.draw.line(SURFACE, (96, 96, 96),  #
                             (0, index), (WIDTH * SIZE, index))  #

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''

1. **화면 크기 설정**: `SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])` 코드에서 `WIDTH`, `HEIGHT`, `SIZE` 변수들은 각각 어떤 역할을 하며, 이 세 변수를 조정함으로써 화면의 크기에 어떤 영향을 미치나요?

2. **세로 줄 그리기**: 세로 줄을 그리는 for 반복문에서 `range(0, WIDTH * SIZE, SIZE)`를 사용하는 이유는 무엇인가요? 이 반복문이 화면에 어떤 결과를 나타내나요?

3. **가로 줄 그리기**: 가로 줄을 그리는 for 반복문에서 `range(0, HEIGHT * SIZE, SIZE)`를 사용하는 이유는 무엇인가요? 세로 줄을 그리는 코드와 어떻게 다르며, 이러한 차이가 시각적으로 어떤 결과를 만들어내나요?

'''
