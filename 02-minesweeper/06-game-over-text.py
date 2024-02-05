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
    largefont = pygame.font.SysFont(None, 72)  # 큰 폰트 생성
    message_over = largefont.render("GAME OVER!!",   # 폰트 사용하여 게임 오버 이미지 생성
                                    True, (0, 255, 225))  # antialias, color
    message_rect = message_over.get_rect()                # 텍스트의 영역 얻기
    message_rect.center = (WIDTH * SIZE / 2, HEIGHT * SIZE / 2)  # 텍스트 영역을 화면의 가운데로 지정

    game_over = False

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
                if field[ypos][xpos] == BOMB:
                    game_over = True

        SURFACE.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE,
                                     (192, 192, 192), rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SURFACE,
                                            (225, 225, 0), rect)

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

        if game_over:                                           # 만약 게임 오버 라면:
            SURFACE.blit(message_over, message_rect.topleft)    # 게임 오버 띄어주기

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''
1. **폰트와 텍스트 렌더링**: `pygame.font.SysFont(None, 72)`을 사용해 큰 폰트를 생성하는 과정에서, `None`과 `72`는 각각 무엇을 의미하나요? 이 코드를 사용하여 게임 오버 메시지를 어떻게 시각적으로 표현할 수 있나요?

2. **텍스트 영역과 중앙 정렬**: `message_rect = message_over.get_rect()`와 `message_rect.center = (WIDTH * SIZE / 2, HEIGHT * SIZE / 2)`를 사용하여 텍스트의 영역을 얻고, 화면 가운데로 위치시키는 과정을 설명해주세요.

3. **게임 오버 시 텍스트 표시**: 게임 오버 상태(`game_over = True`)가 되었을 때, `SURFACE.blit(message_over, message_rect.topleft)`를 사용하여 화면에 게임 오버 메시지를 어떻게 표시하나요? `blit` 메소드는 정확히 무엇을 하며, 이 코드가 게임 플레이 경험에 어떤 영향을 미치나요?
'''
