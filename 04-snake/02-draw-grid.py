import sys

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()


def paint():
    SURFACE.fill((0, 0, 0))

    for index in range(20):                                                             ###
        pygame.draw.line(SURFACE, (64, 64, 64), (index * 30, 0), (index * 30, 600))     ###
        pygame.draw.line(SURFACE, (64, 64, 64), (0, index * 30), (600, index * 30))     ###

    pygame.display.update()


def main():
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

1. **그리드 시스템의 구현**: `pygame.draw.line` 함수를 사용하여 화면에 그리드를 그리는 과정은 어떤 원리로 작동하나요? 이 코드에서 사용된 반복문이 그리드를 생성하는 방식을 설명해 보세요.

2. **좌표 계산과 선 그리기**: `(index * 30, 0)`과 같은 좌표 계산을 통해 선의 시작점과 끝점을 어떻게 결정하나요? 이러한 방식으로 선을 그림으로써 생성되는 그리드의 특성(간격, 방향 등)은 어떻게 조절할 수 있나요?

3. **그래픽 요소의 시각적 속성**: `(64, 64, 64)`와 같이 RGB 값을 사용하여 선의 색상을 지정하는 방식은 게임 디자인에서 어떤 의미를 가지나요? 색상과 선의 두께 등 그래픽 요소의 시각적 속성이 사용자 경험에 미치는 영향에 대해 논의해 보세요.

4. **반복문을 활용한 패턴 생성**: 이 코드에서 반복문을 사용하여 반복적인 패턴(이 경우 그리드)을 생성하는 방식이 프로그래밍에서 어떤 장점을 가지나요? 게임 개발 외의 다른 분야에서 이러한 기법을 활용할 수 있는 예를 생각해 보세요.

\그래픽 요소를 생성하고 조작하는 기본 원리를 이해하는 데 도움이 됩니다. 또한, 게임 개발 과정에서 시각적 요소의 디자인과 구현이 사용자의 시각적 인식과 게임 내 탐색에 어떤 영향을 미치는지에 대한 깊은 이해를 제공할 수 있습니다.
'''