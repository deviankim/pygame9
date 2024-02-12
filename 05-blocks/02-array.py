import sys

import pygame
from pygame.locals import QUIT, Rect


class Block:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self):
        pygame.draw.rect(SURFACE, self.color, self.rect)


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []                             ##################


def main():
    # 삭제 block = Block(color=(255, 0, 0), rect=Rect(100, 50, 80, 30))

    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),    #
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]      #

    for ypos, color in enumerate(colors, start=0):          #
        for xpos in range(0, 5):                            #
            BLOCKS.append(Block(color=color, rect=Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))  #

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))
        for block in BLOCKS:                                #
            block.draw()                                    #

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()

'''

1. **블록 배열의 생성**: 여러 색상의 블록을 생성하는 코드가 어떤 방식으로 작동하는지 설명해주세요. `colors` 리스트와 두 개의 중첩된 반복문을 사용하여 `BLOCKS` 리스트에 `Block` 객체를 추가하는 과정을 분석해 보세요.

2. **`enumerate` 함수의 활용**: `for ypos, color in enumerate(colors, start=0):`에서 `enumerate` 함수를 사용하는 목적이 무엇인가요? `start=0` 파라미터는 어떤 역할을 하며, 이 코드가 블록의 Y 위치를 결정하는 데 어떻게 도움이 되나요?

3. **블록 위치의 계산**: `Block` 객체의 `rect` 파라미터에 전달되는 `Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)` 표현식은 각 블록의 위치와 크기를 어떻게 결정하나요? 이러한 방식으로 블록을 화면에 배치하는 데 있어서의 장점은 무엇인가요?

4. **블록의 시각적 배열**: 생성된 블록들이 화면에 어떤 형태로 배열되나요? 사용된 색상과 반복문을 통해 생성된 블록의 배열이 게임의 시각적 요소에 어떤 영향을 미치는지 설명해보세요.

5. **객체 지향 프로그래밍의 활용**: 이 코드 예제에서 `Block` 클래스의 객체들을 배열로 관리하는 것이 게임 개발에서 어떤 이점을 제공하나요? 게임 내 다양한 요소들을 관리하기 위한 객체 지향 접근 방식의 장점에 대해 논의해 보세요.

6. **블록 그리기**: 모든 블록을 화면에 그리는 과정(`for block in BLOCKS:`)이 어떻게 수행되는지 설명해주세요. 이러한 방식으로 여러 게임 요소를 효과적으로 렌더링하는 것의 중요성을 어떻게 이해할 수 있나요?

Pygame을 사용한 그래픽 프로그래밍, 객체 지향 프로그래밍의 기본 원리, 그리고 게임 개발에서의 다양한 요소 관리와 시각적 표현 방법에 대한 이해를 돕습니다.
'''