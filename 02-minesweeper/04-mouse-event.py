import sys
from math import floor                           # floor 함수를 가져옵니다.
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN  # 마우스 버튼 눌림 이벤트

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENED = 2

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()


def main():
    field = [[EMPTY for xpos in range(WIDTH)]
             for ypos in range(HEIGHT)]

    count = 0
    while count < NUM_OF_BOMBS:

        xpos, ypos = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and \
                    event.button == 1:           # 왼쪽 마우스 버튼이 눌러졌을 때:
                xpos, ypos = floor(event.pos[0] / SIZE), \
                    floor(event.pos[1] / SIZE)   # floor 를 이용해서 xpos, ypos 인덱스 획득
                field[ypos][xpos] = OPENED       # xpos, ypos 위치의 데이터를 OPENED 로 변경

        SURFACE.fill((0, 0, 0))
        for ypos in range(HEIGHT):              # 세로 방향으로 순회
            for xpos in range(WIDTH):           # 가로 방향으로 순회
                tile = field[ypos][xpos]        # 타일값 읽기
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)  # 타일 영역 지정

                if tile == OPENED:              # 타일이 OPENED 값이면:
                    pygame.draw.rect(SURFACE,   # 타일 영역을 회색으로 채운 사각형 그리기.
                                     (192, 192, 192), rect)  #

        for index in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (index, 0), (index, HEIGHT * SIZE))
        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (0, index), (WIDTH * SIZE, index))

        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                if tile == BOMB:
                    rect = pygame.Rect(xpos * SIZE, ypos * SIZE, 10, 10)

                    pygame.draw.ellipse(SURFACE, (222, 100, 0), rect)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''

1. **floor 함수 사용 이유**: 코드에서 `floor(event.pos[0] / SIZE)`와 같이 `floor` 함수를 사용하는 이유는 무엇인가요? 특히, 마우스 클릭 위치를 기반으로 xpos와 ypos 인덱스를 계산할 때, 이 함수가 어떤 역할을 하나요?

2. **마우스 버튼 눌림 이벤트 처리**: `if event.type == MOUSEBUTTONDOWN and event.button == 1:` 조건문은 어떤 사용자 동작을 감지하나요? 여기서 `event.button == 1`은 구체적으로 어떤 마우스 버튼을 의미하나요?

3. **타일 영역 지정**: `rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)`에서 각각의 요소는 어떤 의미를 가지나요? 이 코드가 게임 내에서 어떤 역할을 하는지 설명해 주세요.

4. **타일 상태 변경 로직**: `field[ypos][xpos] = OPENED` 코드는 어떤 상황에서 실행되나요? 이 코드의 목적은 무엇이며, 이 변경이 게임 진행에 어떤 영향을 미치나요?

5. **타일 그리기 로직**: `if tile == OPENED:` 조건문 아래에 있는 `pygame.draw.rect(SURFACE, (192, 192, 192), rect)` 코드는 어떤 기능을 수행하나요? 이 코드가 실행되면 화면에는 어떤 변화가 일어나나요?

'''
