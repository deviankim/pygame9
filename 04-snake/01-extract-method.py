import sys

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()


def paint():                    ######
    SURFACE.fill((0, 0, 0))     ######
    pygame.display.update()     ######


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        paint()                 ######

        FPSCLOCK.tick(5)


if __name__ == '__main__':
    main()


'''

1. **함수 분리의 목적**: `paint` 함수를 따로 정의하여 게임 루프에서 호출하는 방식이 갖는 장점은 무엇인가요? 함수를 분리하여 코드를 구성하는 것이 프로그램의 가독성과 유지 보수성에 어떻게 기여하나요?

2. **화면 업데이트 방식**: `SURFACE.fill((0, 0, 0))`와 `pygame.display.update()`를 사용하여 화면을 업데이트하는 과정에서, Pygame에서 화면을 깨끗하게 지우고 다시 그리는 과정이 왜 필요한가요? 이러한 방식이 게임의 그래픽 표현에 어떤 영향을 미치나요?

3. **프레임 레이트 조절**: `FPSCLOCK.tick(5)`를 통해 게임의 프레임 레이트를 조절하는 이유는 무엇인가요? 프레임 레이트가 게임 플레이와 사용자 경험에 어떤 영향을 미치며, 어떻게 적절한 프레임 레이트를 결정할 수 있나요?

4. **게임 루프와 이벤트 처리**: `main` 함수 내의 게임 루프에서 이벤트를 처리하는 방식과 `paint` 함수를 호출하는 구조는 어떤 작업을 수행하나요? 게임 루프와 이벤트 처리의 개념을 어떻게 이해할 수 있으며, 이것이 게임 프로그래밍에서 왜 중요한가요?

코드의 구조화, 화면 렌더링, 프레임 레이트 조절, 그리고 게임 루프의 작동 원리를 이해하는 데 도움이 됩니다. 또한, 이러한 기초적인 개념과 기법들이 게임의 퍼포먼스와 사용자 경험에 어떻게 영향을 미치는지에 대한 깊은 통찰력을 제공할 수 있습니다.
'''