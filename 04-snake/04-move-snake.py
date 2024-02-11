import sys
import random
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN  #

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()

FOODS = []
SNAKE = []                                                                  #
(W, H) = (20, 20)


def add_food():
    while True:
        pos = (random.randint(0, W - 1), random.randint(0, H - 1))
        FOODS.append(pos)
        break


def paint():
    SURFACE.fill((0, 0, 0))
    for food in FOODS:
        pygame.draw.ellipse(SURFACE, (0, 255, 0),
                            Rect(food[0] * 30, food[1] * 30, 30, 30))
    for body in SNAKE:                                                      #
        pygame.draw.rect(SURFACE, (0, 255, 255),                            #
                         Rect(body[0] * 30, body[1] * 30, 30, 30))          #
    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64), (index * 30, 0), (index * 30, 600))
        pygame.draw.line(SURFACE, (64, 64, 64), (0, index * 30), (600, index * 30))

    pygame.display.update()


def main():
    key = K_DOWN                                                            #
    SNAKE.append((int(W / 2), int(H / 2)))                                  #
    for _ in range(10):
        add_food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:                                     #
                key = event.key                                             #

        if key == K_LEFT:                                                   #
            head = (SNAKE[0][0] - 1, SNAKE[0][1])                           #
        elif key == K_RIGHT:                                                #
            head = (SNAKE[0][0] + 1, SNAKE[0][1])                           #
        elif key == K_UP:                                                   #
            head = (SNAKE[0][0], SNAKE[0][1] - 1)                           #
        elif key == K_DOWN:                                                 #
            head = (SNAKE[0][0], SNAKE[0][1] + 1)                           #
                                                                            #
        SNAKE.insert(0, head)                                               #
        SNAKE.pop()                                                         #

        paint()

        FPSCLOCK.tick(5)


if __name__ == '__main__':
    main()

'''

1. **뱀의 이동 메커니즘**: `SNAKE.append((int(W / 2), int(H / 2)))`에서 시작하는 `SNAKE` 리스트에 뱀의 몸통을 추가하는 방법은 게임의 어떤 핵심 메커니즘을 구현하나요? 이 코드가 뱀 게임에서 뱀의 초기 위치와 이동을 어떻게 관리하는지 설명해 보세요.

2. **키 입력에 따른 방향 변경**: 사용자의 키 입력(`KEYDOWN`)을 감지하여 뱀의 이동 방향을 변경하는 로직(`if key == K_LEFT:` 등)은 어떻게 작동하나요? 이벤트 처리를 통해 게임 내 객체의 동작을 제어하는 방법에 대해 설명해 보세요.

3. **뱀 몸통의 그래픽 표현**: `for body in SNAKE:` 루프를 사용하여 뱀의 몸통을 화면에 표시하는 과정은 어떤 원리로 작동하나요? `pygame.draw.rect`를 사용하여 뱀 몸통을 그리는 방식이 게임의 시각적 요소와 플레이어의 시각적 인식에 어떤 영향을 미치는지 논의해 보세요.

4. **뱀의 성장과 이동 제어**: 뱀의 머리를 리스트의 첫 번째 요소로 추가하고, 마지막 요소를 제거하는 방식(`SNAKE.insert(0, head)` 및 `SNAKE.pop()`)이 뱀의 이동을 어떻게 구현하나요? 이 방식이 뱀의 길이를 일정하게 유지하면서도 이동을 가능하게 하는 메커니즘을 어떻게 설명할 수 있나요?

5. **게임 루프와 프레임 레이트의 관리**: `FPSCLOCK.tick(5)`를 통해 게임의 프레임 레이트를 조절하는 것이 게임 플레이의 유동성과 반응성에 어떤 영향을 미치나요? 프레임 레이트가 게임의 난이도와 사용자 경험에 미치는 영향에 대해 설명해 보세요.

게임 프로그래밍의 기본적인 요소, 특히 이벤트 기반의 입력 처리, 객체의 그래픽 표현, 그리고 게임의 동작 로직 구현에 대한 이해를 심화할 수 있도록 돕습니다. 또한, 게임의 기본적인 상호작용 메커니즘과 사용자 인터페이스 디자인에 대한 깊은 통찰력을 제공할 것입니다.
'''