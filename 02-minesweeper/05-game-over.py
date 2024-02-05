import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

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
    game_over = False   # 게임 오버 변수를 False 로 정해 둔다. 이 코드를 생략하면?

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
                    event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE), \
                    floor(event.pos[1] / SIZE)
                if field[ypos][xpos] == BOMB:   # 클릭한 곳이 폭탄이면
                    game_over = True            # 게임 오버

        SURFACE.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:   # 타일을 손대지 않았거나 폭탄이면:
                    pygame.draw.rect(SURFACE,
                                     (192, 192, 192), rect)
                    if game_over and tile == BOMB:      # 게임 오버일 경우 폭탄 표시
                        pygame.draw.ellipse(SURFACE,    # 폭탄을 큰 원으로 표시
                                            (225, 225, 0), rect)  #

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
1. **게임 오버 변수의 목적**: `game_over = False`라고 설정한 이유는 무엇인가요? 만약 이 코드를 생략한다면, 게임의 흐름에 어떤 영향을 미칠까요?

2. **클릭한 곳이 폭탄일 경우의 처리**: 사용자가 마우스로 클릭한 위치에 폭탄이 있는 경우 `game_over = True`로 설정됩니다. 이 로직이 게임 내에서 어떤 중요한 역할을 하나요? 그리고 이를 통해 사용자에게 어떤 피드백을 주는 것이 중요한가요?

3. **폭탄 타일의 시각적 표현**: 게임 오버 상태에서 폭탄 타일을 큰 원으로 표시하는 이유는 무엇인가요(`pygame.draw.ellipse(SURFACE, (225, 225, 0), rect)`)? 이 시각적 표현이 사용자 경험에 어떤 영향을 미치나요?

'''
