import sys

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()

'''

1. **pygame 초기화**: `pygame.init()` 함수는 pygame 프로그램을 시작하기 전에 어떤 작업을 수행하나요? 모든 pygame 애플리케이션에서 이 함수를 호출하는 것이 필수인 이유는 무엇인가요?

2. **화면 설정**: `SURFACE = pygame.display.set_mode((800, 800))` 코드는 프로그램 내에서 어떤 역할을 합니다? 여기서 `(800, 800)`은 무엇을 의미하며, 이 값을 변경하면 어떤 결과가 발생하나요?

3. **이벤트 처리**: `for event in pygame.event.get():` 루프에서 `if event.type == QUIT:` 조건은 어떤 이벤트를 처리하기 위한 것이며, 이 조건이 충족되었을 때 실행되는 `pygame.quit()`와 `sys.exit()` 함수는 각각 어떤 작업을 수행하나요?

4. **화면 갱신**: `pygame.display.update()` 함수의 호출 목적은 무엇인가요? 이 함수는 어떤 시점에 호출되어야 하며, 호출되지 않는다면 어떤 문제가 발생하나요?

5. **프레임 속도 제어**: `FPSCLOCK.tick(20)` 구문은 프로그램의 실행 속도에 어떤 영향을 미치나요? 여기서 `20`은 어떤 의미를 가지며, 이 값을 변경하면 게임의 어떤 측면에 영향을 미치나요?

pygame 라이브러리의 기본적인 사용 방법과 게임 루프의 핵심 개념을 이해하는 데 도움을 줍니다. 또한, 게임 개발 과정에서 이벤트 처리, 화면 갱신, 프레임 속도 제어 등의 중요성을 강조합니다.
'''
