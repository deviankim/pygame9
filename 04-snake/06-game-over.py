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


def paint(message):         ######
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

    if message != None:                     ######
        SURFACE.blit(message, (150, 300))   ######
    pygame.display.update()


def main():
    myfont = pygame.font.SysFont(None, 80)  ######
    key = K_DOWN
    message = None                          ######
    game_over = False                       ######
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

        if not game_over:                               ######
            if key == K_LEFT:                           # 들여쓰기만
                head = (SNAKE[0][0] - 1, SNAKE[0][1])   # 들여쓰기만
            elif key == K_RIGHT:                        # 들여쓰기만
                head = (SNAKE[0][0] + 1, SNAKE[0][1])   # 들여쓰기만
            elif key == K_UP:                           # 들여쓰기만
                head = (SNAKE[0][0], SNAKE[0][1] - 1)   # 들여쓰기만
            elif key == K_DOWN:                         # 들여쓰기만
                head = (SNAKE[0][0], SNAKE[0][1] + 1)   # 들여쓰기만

            if head in SNAKE or \
                    head[0] < 0 or head[0] >= W or \
                    head[1] < 0 or head[1] >= H:                                ###### 코드 추가
                message = myfont.render("Game Over!",     True, (255, 255, 0))  ###### 코드 추가
                game_over = True                                                ###### 코드 추가

            SNAKE.insert(0, head)                       # 들여쓰기만
            if head in FOODS:                           # 들여쓰기만
                move_food(head)                         # 들여쓰기만
            else:                                       # 들여쓰기만
                SNAKE.pop()                             # 들여쓰기만

        paint(message)                                  # message 파라메터 추가

        FPSCLOCK.tick(5)


if __name__ == '__main__':
    main()


'''

1. **`paint` 함수에 `message` 파라메터 추가**: `paint` 함수에서 `message` 파라메터를 추가한 이유는 무엇인가요? 이 변경이 게임의 UI에 어떤 영향을 미치나요?

2. **`message` 변수의 활용**: 게임 오버 시 `message` 변수에 "Game Over!" 문자열을 저장하고 화면에 표시하는 과정은 어떻게 구현되나요? 이 방식이 사용자 경험에 어떤 영향을 주나요?

3. **게임 오버 조건**: 게임 오버의 조건을 확인하는 로직(`if head in SNAKE or head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H:`)이 어떻게 작동하는지 설명할 수 있나요? 이 조건들이 게임의 규칙과 플레이 영역을 어떻게 정의하나요?

4. **폰트 사용하여 메시지 표시**: `myfont.render("Game Over!", True, (255, 255, 0))` 호출을 통해 게임 오버 메시지를 화면에 표시하는 과정에서, 폰트 객체를 사용하는 방법과 메시지 표시의 시각적 요소(색상 등)를 커스터마이징하는 방법을 설명해주세요.

5. **`paint` 함수 내에서 조건부 메시지 표시**: `paint` 함수 내에서 `if message != None:` 조건을 사용하여 게임 오버 메시지를 조건부로 표시하는 로직의 필요성과 효과에 대해 설명해주세요. 이 구현이 게임 상태(진행 중 vs 게임 오버)에 따른 UI 변화를 어떻게 관리하나요?

조건문, 함수 파라메터와 인수, UI 업데이트와 같은 기본적인 프로그래밍 개념과 게임 디자인 원리에 대한 이해를 돕습니다.
'''