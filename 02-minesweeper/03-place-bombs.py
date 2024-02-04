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

# Q1. 폭탄 수 조정하기: 만들어지는 폭탄수를 10개 더 추가하려면 어떻게 해야 할까요?
# Q2. 화면 크기 변경하기: 게임의 가로 너비를 25 칸으로 늘리려면 어떤 코드를 수정해야 할까요?
# Q3. 프레임 속도 조정하기: 게임의 프레임 속도를 초당 30 프레임으로 변경하려면 어디를 수정해야 할까요?
# Q4. 폭탄 그리기 변경하기: 폭탄을 그리는 원의 크기를 더 크게 하려면 어떤 부분을 수정해야 할까요?
# Q5. 게임 종료 조건 추가하기: 사용자가 게임 창을 닫을 때 이외에도, 특정 키(예: ESC 키)를 눌러 게임을 종료하려면 어떤 코드를 추가해야 할까요?
