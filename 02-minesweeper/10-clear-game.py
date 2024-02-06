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
OPEN_COUNT = 0      #######################################################
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
    global OPEN_COUNT   #######################################################
    if CHECKED[y_pos][x_pos]:
        return

    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                    field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1  #######################################################
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and \
                        not (xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)


def main():
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!",        ##############################
                                     True, (0, 255, 225))  ####################
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

        if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMBS:         ###########################
            SURFACE.blit(message_clear, message_rect.topleft)   ################################
        elif game_over:                                         #######################################
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''

1. **OPEN_COUNT 변수의 사용**: `OPEN_COUNT` 변수는 코드 내에서 어떤 역할을 하며, 왜 필요한가요? 이 변수가 게임 로직에서 어떻게 활용되는지 설명해 주세요.

2. **게임 상태 메시지**: `message_clear`와 `message_over` 변수는 각각 어떤 상황에서 사용되나요? 이 메시지들이 게임의 사용자 인터페이스에 어떤 영향을 미치며, 왜 중요한가요?

3. **타일 열기 메커니즘**: `open_tile` 함수에서 재귀적으로 타일을 열 때, 어떤 조건을 검사하나요? 이 로직이 지뢰 찾기 게임에서 어떤 기능을 수행하는지 설명해 주세요.

4. **게임 클리어 조건**: 게임 클리어 조건(`if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMBS:`)은 구체적으로 어떻게 계산되나요? 이 조건이 참이 될 때, 사용자에게 어떤 피드백을 제공하나요?

5. **글로벌 변수 사용**: `open_tile` 함수 내에서 `global OPEN_COUNT`를 선언하는 이유는 무엇인가요? 글로벌 변수를 사용할 때 주의해야 할 점은 무엇이며, 이 경우에는 왜 사용되었나요?

'''
