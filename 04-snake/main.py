import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_s, K_d, K_w, Rect

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()

FOODS = []
SNAKE = []
(W, H) = (20, 20)


def add_food():
    ''' 임의의 장소에 먹이를 배치'''

    while True:
        pos = (random.randint(0, W - 1), random.randint(0, H - 1))
        if pos in FOODS or pos in SNAKE:
            continue

        FOODS.append(pos)
        break


def move_food(pos):
    ''' 먹이를 다른 장소로 이동'''
    i = FOODS.index(pos)
    del FOODS[i]
    add_food()


def paint(message):
    SURFACE.fill((0, 0, 0))
    for food in FOODS:
        pygame.draw.ellipse(SURFACE, (0, 255, 0), Rect(food[0] * 30, food[1] * 30, 30, 30))

    for body in SNAKE:
        pygame.draw.rect(SURFACE, (0, 255, 255), Rect(body[0] * 30, body[1] * 30, 30, 30))

    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64), (index * 30, 0), (index * 30, 600))
    if message != None:
        SURFACE.blit(message, (150, 300))
    pygame.display.update()


def main():
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    SNAKE.append((int(W / 2), int(H / 2)))

    for _ in range(10):
        add_food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        if not game_over:
            (sx, sy) = (SNAKE[0][0], SNAKE[0][1])
            if key in [K_LEFT, K_a]:
                head = (sx - 1, sy)
            elif key in [K_RIGHT, K_d]:
                head = (sx + 1, sy)
            elif key in [K_UP, K_w]:
                head = (sx, sy - 1)
            elif key in [K_DOWN, K_s]:
                head = (sx, sy + 1)

            if head in SNAKE or \
                    head[0] < 0 or head[0] >= W or \
                    head[1] < 0 or head[1] >= H:
                message = myfont.render("Game Over!!", True, (255, 255, 0))

                game_over = True

            SNAKE.insert(0, head)
            if head in FOODS:
                move_food(head)
            else:
                SNAKE.pop()

        paint(message)
        FPSCLOCK.tick(5)


if __name__ == '__main__':
    main()
