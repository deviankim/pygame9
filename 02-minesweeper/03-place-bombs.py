import sys
from random import randint  # randint 사용을 위한 import
import pygame
from pygame.locals import QUIT

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20   # 전체 폭탄 수
EMPTY = 0           # 칸 상태: 비었음
BOMB = 1            # 칸 상태: 폭탄
OPENED = 2          # 칸 상태: 열었음

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()


def main():
    # 2중 배열 field 생성, 크기는 WIDTH 만한게 HEIGHT 만큼이다.
    field = [[EMPTY for xpos in range(WIDTH)]   #
             for ypos in range(HEIGHT)]         #

    # 폭탄을 설치
    count = 0                       # 폭탄수 카운팅 변수
    while count < NUM_OF_BOMBS:     # 지정한 폭탄수(NUM_OF_BOMBS) 만큼 만들도록 조건 지정
        # 무작위로 x,y 좌표 얻어 오기
        xpos, ypos = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)  #
        if field[ypos][xpos] == EMPTY:      # 배열이 비어 있어야 폭탄을 배치 한다.
            field[ypos][xpos] = BOMB        # 배열에 폭탄값 넣기
            count += 1                      # 폭탄수 증가

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        for index in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (index, 0), (index, HEIGHT * SIZE))
        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (0, index), (WIDTH * SIZE, index))

        # 디버깅 용으로 폭탄의 위치를 보여준다.
        for ypos in range(HEIGHT):          #
            for xpos in range(WIDTH):       #
                tile = field[ypos][xpos]    #
                if tile == BOMB:            # 현재 타일이 폭탄인 경우에 폭탄을 그려준다.
                    # 폭탄 마킹용 rect 위치/사이즈 지정
                    rect = pygame.Rect(xpos * SIZE, ypos * SIZE, 10, 10)     #
                    # 오렌지색원 그리기
                    pygame.draw.ellipse(SURFACE, (222, 100, 0), rect)  #

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()
