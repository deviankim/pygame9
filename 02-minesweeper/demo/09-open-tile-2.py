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
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()


def num_of_bomb(field, x_pos, y_pos):
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                    field[ypos][xpos] == BOMB:
                count += 1
    return count


def open_tile(field, x_pos, y_pos):
    if CHECKED[y_pos][x_pos]:
        return

    CHECKED[y_pos][x_pos] = True
    # field[ypos][xpos] = OPENED  # 이제 여기서 마킹하지 않고 for loop 에서 처리해야 한다.

    for yoffset in range(-1, 2):                                # y좌표 [-1, 0, +1]
        for xoffset in range(-1, 2):                            # x좌표 [-1, 0, +1]
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)     # 실제 검사할 좌표
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                    field[ypos][xpos] == EMPTY:                 # 좌표 범위가 화면내 and EMPTY:
                field[ypos][xpos] = OPENED                      # OPENED 로 마킹
                count = num_of_bomb(field, xpos, ypos)          # 주변 폭탄 개수 구하기
                if count == 0 and \
                        not (xpos == x_pos and ypos == y_pos):  # 주변에 폭탄이 없고, 좌표가 기준점이 아니라면:
                    open_tile(field, xpos, ypos)                # open_tile 또 열기(재귀)


def main():
    smallfont = pygame.font.SysFont(None, 36)
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
                else:
                    open_tile(field, xpos, ypos)

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
                elif tile == OPENED:
                    count = num_of_bomb(field, xpos, ypos)
                    if count > 0:
                        num_image = smallfont.render(
                            "{}".format(count), True, (255, 255, 0))
                        SURFACE.blit(num_image,
                                     (xpos * SIZE + 10, ypos * SIZE + 10))

        for index in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (index, 0), (index, HEIGHT * SIZE))
        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (0, index), (WIDTH * SIZE, index))

        if game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''

1. **재귀 함수 사용 이유**: `open_tile` 함수 내에서 재귀 호출을 사용하는 이유는 무엇인가요? 주변 타일을 자동으로 열기 위한 조건(`if count == 0 and not (xpos == x_pos and ypos == y_pos)`)은 어떤 상황을 처리하기 위해 필요한가요?

2. **타일 상태 업데이트 로직**: `open_tile` 함수에서 `CHECKED` 배열과 `field` 배열의 상태를 변경하는 로직은 어떤 목적으로 작성되었나요? `CHECKED` 배열이 왜 필요하며, 게임의 어떤 기능을 지원하나요?

'''
