import sys
import random
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()

FOODS = []
SNAKE = []
(W, H) = (20, 20)


def add_food():
    while True:
        pos = (random.randint(0, W - 1), random.randint(0, H - 1))
        if pos in FOODS or pos in SNAKE:
            continue
        FOODS.append(pos)
        break


def move_food(pos):
    i = FOODS.index(pos)
    del FOODS[i]
    add_food()


def paint():
    SURFACE.fill((0, 0, 0))
    for food in FOODS:
        pygame.draw.ellipse(SURFACE, (0, 255, 0),
                            Rect(food[0] * 30, food[1] * 30, 30, 30))
    for body in SNAKE:
        pygame.draw.rect(SURFACE, (0, 255, 255),
                         Rect(body[0] * 30, body[1] * 30, 30, 30))
    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64), (index * 30, 0), (index * 30, 600))
        pygame.draw.line(SURFACE, (64, 64, 64), (0, index * 30), (600, index * 30))

    pygame.display.update()


def main():
    key = K_DOWN
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

        if key == K_LEFT:
            head = (SNAKE[0][0] - 1, SNAKE[0][1])
        elif key == K_RIGHT:
            head = (SNAKE[0][0] + 1, SNAKE[0][1])
        elif key == K_UP:
            head = (SNAKE[0][0], SNAKE[0][1] - 1)
        elif key == K_DOWN:
            head = (SNAKE[0][0], SNAKE[0][1] + 1)

        SNAKE.insert(0, head)
        if head in FOODS:
            move_food(head)
        else:
            SNAKE.pop()

        paint()

        FPSCLOCK.tick(5)


if __name__ == '__main__':
    main()

