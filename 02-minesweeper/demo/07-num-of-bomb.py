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


def num_of_bomb(field, x_pos, y_pos):   # field, x_pos, y_pos 를 파라메터로 받는 함수
    count = 0                           # 반환할 count 를 0으로 초기화
    for yoffset in range(-1, 2):        # 윗쪽 한칸부터 아래 한칸까지 순회
        for xoffset in range(-1, 2):    # 좌측 한칸부터 우측 한칸까지 순회
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)     # 실제 계산할 절대 인덱스 구하기
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                    field[ypos][xpos] == BOMB:                  # 만약 범위내이면서 폭탄이면:
                count += 1                                      # count 증가
    return count                        # count 리턴


def main():
    smallfont = pygame.font.SysFont(None, 36)  # 지뢰 갯수를 출력하기 위한 폰트
    largefont = pygame.font.SysFont(None, 72)
    message_over = largefont.render("GAME OVER!!",
                                    True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (WIDTH * SIZE / 2, HEIGHT * SIZE / 2)

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
                else:                                       # 폭탄이 아닌 영역에 숫자 출력한다.
                    count = num_of_bomb(field, xpos, ypos)  # 폭탄 개수를 함수로 구함
                    num_image = smallfont.render(           # 폭탄 개수 이미지 생성
                        "{}".format(count), True, (255, 255, 0))  #
                    SURFACE.blit(num_image,                 # 개수 그리기
                                 (xpos * SIZE + 10, ypos * SIZE + 10))  # 그릴 좌표

        if game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''
1. **폭탄 개수 계산 함수**: `num_of_bomb` 함수는 어떤 역할을 하나요? 주어진 위치 `x_pos`, `y_pos` 주변에 있는 폭탄의 개수를 계산하는 과정에서, 왜 `-1`에서 `2` 범위의 `for` 루프를 사용하나요?

2. **폭탄 개수 표시**: 게임 내에서 폭탄이 아닌 타일에 주변 폭탄의 개수를 표시하는 이유는 무엇인가요? 이 기능이 지뢰찾기 게임의 전략적 요소에 어떻게 기여하나요?
'''
