import sys
import random                                                       #
import pygame
from pygame.locals import QUIT, Rect                                #

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()

FOODS = []                                                          #
(W, H) = (20, 20)                                                   #


def add_food():                                                     #
    while True:                                                     #
        pos = (random.randint(0, W - 1), random.randint(0, H - 1))  #
        FOODS.append(pos)                                           #
        break                                                       #


def paint():
    SURFACE.fill((0, 0, 0))
    for food in FOODS:                                                  #
        pygame.draw.ellipse(SURFACE, (0, 255, 0),                       #
                            Rect(food[0] * 30, food[1] * 30, 30, 30))   #
    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64), (index * 30, 0), (index * 30, 600))
        pygame.draw.line(SURFACE, (64, 64, 64), (0, index * 30), (600, index * 30))

    pygame.display.update()


def main():
    for _ in range(10):                                                 #
        add_food()                                                      #

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        paint()

        FPSCLOCK.tick(5)


if __name__ == '__main__':
    main()


'''

1. **음식 생성 알고리즘**: `add_food` 함수는 어떻게 작동하며, `random.randint(0, W - 1)`을 사용하여 음식의 위치를 결정하는 과정에서 어떤 고려사항이 있나요? 이 방식이 게임 화면 내에서 음식이 무작위 위치에 나타나게 하는 원리를 설명해 보세요.

2. **무작위 요소의 게임 내 역할**: `add_food` 함수를 통해 게임에 무작위 요소를 추가하는 것이 게임 플레이에 어떻게 영향을 미치나요? 무작위로 생성된 음식이 게임의 재미와 도전 정도에 어떤 변화를 주는지 논의해 보세요.

3. **Rect 객체와 그래픽 표현**: `pygame.draw.ellipse` 함수와 `Rect` 객체를 사용하여 음식을 화면에 어떻게 표현하나요? `Rect(food[0] * 30, food[1] * 30, 30, 30)`에서 각 인자가 의미하는 바와, 이를 통해 생성되는 타원의 위치와 크기에 대해 설명해 보세요.

4. **FOODS 리스트의 활용**: 게임 시작 시 `FOODS` 리스트에 음식 위치를 10개 추가하는 과정이 게임의 초기 상태 설정에 어떻게 기여하나요? 이 리스트를 관리하고 업데이트하는 방법이 게임의 다이내믹을 어떻게 조절할 수 있는지 고려해 보세요.

5. **게임 화면의 그리드와 음식의 배치**: 그리드 시스템에 음식을 배치하는 방식이 게임의 시각적 구성과 플레이어의 전략 수립에 어떤 영향을 미치나요? 게임 화면을 그리드로 나누어 관리하는 것이 게임 디자인에서 왜 중요한지 탐구해 보세요.

무작위 요소의 중요성, 게임 객체의 그래픽 표현 방법, 그리고 게임 화면의 구조적 관리 방법에 대해 이해하는 데 도움을 줍니다. 또한, 이러한 요소들이 게임의 재미와 플레이어의 경험을 어떻게 증진시키는지에 대한 통찰력을 제공할 수 있습니다.
'''