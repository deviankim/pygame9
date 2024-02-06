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
OPEN_COUNT = 0      # 열린 타일의 개수를 합산하여 게임이 클리어 되었는지 확인하는 용도
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
    global OPEN_COUNT                                   # global 변수를 사용하기 위해 반드시 필요하다.
    if CHECKED[y_pos][x_pos]:
        return

    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                    field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1                         # 열린 타일 수 누적
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and \
                        not (xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)


def main():
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!",        # 게임 클리어 메시지 준비
                                     True, (0, 255, 225))  #
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

        if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMBS:         # 열 수 있는 타일이 모두 열렸다면:
            SURFACE.blit(message_clear, message_rect.topleft)   # "!!CLEARED!!" 출력
        elif game_over:                                         # elif 조건 처리
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''

1. **OPEN_COUNT의 역할**: `OPEN_COUNT` 변수는 코드 내에서 어떤 역할을 합니다? 이 변수를 사용하여 게임의 어떤 상태를 결정하나요?

2. **함수와 글로벌 변수**: `open_tile` 함수에서 `OPEN_COUNT` 글로벌 변수를 사용하는 이유는 무엇인가요? 재귀 호출 과정에서 이 변수를 어떻게 활용하며, 왜 함수 내에서 글로벌 변수를 사용해야 하는 상황이 발생하나요?

3. **게임 클리어 조건**: 게임이 클리어되었을 때 출력되는 메시지를 결정하는 로직은 어떻게 작동하나요? `if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMBS:` 조건문이 의미하는 바는 무엇이며, 이 조건이 충족되었을 때 사용자에게 어떤 피드백을 제공하나요?

'''
