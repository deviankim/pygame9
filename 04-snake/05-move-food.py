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
        if pos in FOODS or pos in SNAKE:    #
            continue                        #
        FOODS.append(pos)
        break


def move_food(pos):         #
    i = FOODS.index(pos)    #
    del FOODS[i]            #
    add_food()              #


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
        if head in FOODS:       #
            move_food(head)     #
        else:                   #
            SNAKE.pop()         #

        paint()

        FPSCLOCK.tick(5)


if __name__ == '__main__':
    main()

'''

1. **음식 추가 메커니즘**: `add_food` 함수 내에서 `pos in FOODS or pos in SNAKE` 조건을 사용하는 이유는 무엇인가요? 이 로직이 게임 내에서 음식이 뱀의 몸통이나 다른 음식과 겹치지 않게 배치되는 방식에 어떻게 기여하나요?

2. **음식 이동 메커니즘**: `move_food` 함수를 통해 특정 음식을 새 위치로 이동시키는 과정은 어떻게 작동하나요? 특정 음식을 리스트에서 제거한 후 새로운 음식을 추가하는 과정이 게임 동작에 어떤 다이내믹을 추가하나요?

3. **뱀의 성장 로직**: 뱀이 음식을 먹었을 때 (`if head in FOODS:`)와 먹지 않았을 때 (`else: SNAKE.pop()`)의 처리가 어떻게 다른가요? 이 조건문이 뱀의 성장을 구현하는 메커니즘을 어떻게 설명할 수 있나요?

4. **게임의 진행 조건**: `if pos in FOODS or pos in SNAKE:` 조건에서 음식을 추가할 위치를 결정하는 데 있어서 뱀의 위치를 고려하는 이유는 무엇인가요? 이 조건이 게임의 플레이 영역과 상호작용을 어떻게 관리하나요?

5. **음식 위치의 무작위성**: `random.randint(0, W - 1), random.randint(0, H - 1)`을 사용하여 음식의 위치를 무작위로 결정하는 방식이 게임 플레이에 어떤 영향을 미치나요? 무작위성이 게임의 재미와 재도전 가치에 어떻게 기여하나요?

게임 개발의 기본적인 개념들—조건문, 리스트 조작, 무작위성의 활용—을 이해하는 데 도움을 주며, 간단한 게임을 만들며 학습하는 과정에서 중요한 사고 과정과 문제 해결 능력을 개발할 수 있도록 합니다.
'''