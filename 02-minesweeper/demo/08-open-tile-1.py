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
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]  # 이미 클릭했는지 여부 저장

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


def open_tile(field, x_pos, y_pos):     # 폭탄이 아닌 경우 타일을 여는 함수
    if CHECKED[y_pos][x_pos]:           # 이미 열린 경우:
        return                          # 아무 것도 하지 않음
                                        #
    CHECKED[y_pos][x_pos] = True        # 열었음을 알 수 있게 True 설정
    field[y_pos][x_pos] = OPENED        # field 도 OPENED 로 변경하여 렌더링시 활용


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
                else:                               # 클릭한 타일이 폭탄이 아니면:
                    open_tile(field, xpos, ypos)    # 타일 열기

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
                elif tile == OPENED:                        # 타일이 열려 있으면: (아래의 디버깅 코드와 동일)
                    count = num_of_bomb(field, xpos, ypos)  # 폭탄의 개수 계산
                    if count > 0:                           # 폭탄이 하나 이상인것만 개수를 표시한다.
                        num_image = smallfont.render(       # 폭탄 개수 이미지로 생성
                            "{}".format(count), True, (255, 255, 0))  #
                        SURFACE.blit(num_image,             # 이미지 출력
                                     (xpos * SIZE + 10, ypos * SIZE + 10))     #

        for index in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (index, 0), (index, HEIGHT * SIZE))
        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (0, index), (WIDTH * SIZE, index))

        # 이제 디버깅용 코드를 제거할 때가 되었습니다. 아래 주석으로 표시한 부분을 제거해주세요.
        # for ypos in range(HEIGHT):
        #     for xpos in range(WIDTH):
        #         tile = field[ypos][xpos]
        #         if tile == BOMB:
        #             rect = pygame.Rect(xpos * SIZE, ypos * SIZE, 10, 10)
        #
        #             pygame.draw.ellipse(SURFACE, (222, 100, 0), rect)
        #        else:
        #            count = num_of_bomb(field, xpos, ypos)
        #            num_image = smallfont.render(
        #                "{}".format(count), True, (255, 255, 0))
        #            SURFACE.blit(num_image,
        #                         (xpos * SIZE + 10, ypos * SIZE + 10))

        if game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

'''

1. **타일 열기 메커니즘**: `open_tile` 함수 내에서 `CHECKED` 배열을 사용하는 목적은 무엇인가요? 

2. **주변 폭탄 개수 표시**: 타일이 열렸을 때 주변의 폭탄 개수를 계산하고 표시하는 과정을 어떻게 구현했나요?

'''
