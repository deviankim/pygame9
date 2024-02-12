import math     ######
import random   ######
import sys

import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT


class Block:
    def __init__(self, color, rect, speed=0):           ######
        self.color = color
        self.rect = rect
        self.speed = speed                              ######
        self.dir = random.randint(-45, 45) + 270        ######

    def move(self):                                                         #
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed  #
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed  #

    def draw(self):
        if self.speed == 0:                                         #
            pygame.draw.rect(SURFACE, self.color, self.rect)        #
        else:                                                       #
            pygame.draw.ellipse(SURFACE, self.color, self.rect)     #


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10)     ######


def main():
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color=color, rect=Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    PADDLE.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    PADDLE.rect.centerx += 10
        if BALL.rect.centery < 1000:                        ######
            BALL.move()                                     ######

        SURFACE.fill((0, 0, 0))
        BALL.draw()                                         ######
        PADDLE.draw()
        for block in BLOCKS:
            block.draw()

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()

'주석이 붙은 코드는 새로 추가된 코드야. 새로 추가된 코드를 위주로 교육용 질문을 몇 개 만들어 줘'

'''
새로 추가된 코드를 중심으로 만들 수 있는 교육용 질문은 다음과 같습니다:

1. **블록 클래스의 확장**: `Block` 클래스에 `speed`와 `dir` 속성을 추가함으로써, 이 클래스는 어떻게 더 다양한 종류의 게임 요소를 표현할 수 있게 되었나요? 이러한 변경이 게임의 어떤 측면에 영향을 미칠 수 있나요?

2. **객체의 움직임 구현**: `move` 메서드는 `Block` 객체를 어떻게 움직이게 만드나요? `math.cos`와 `math.sin` 함수를 사용하여 방향을 계산하는 과정을 설명해주세요.

3. **다양한 그래픽 요소의 표현**: `draw` 메서드 내에서 `speed` 속성의 값에 따라 사각형과 원을 다르게 그리는 조건은 무엇을 의미하나요? 이러한 조건적 표현이 게임 디자인에 어떻게 적용될 수 있나요?

4. **수학적 계산과 게임 프로그래밍**: `move` 메서드에서 사용된 수학적 계산이 게임 개발에서 어떤 역할을 하는지 탐구해보세요. 각도와 속도를 사용하여 객체의 움직임을 계산하는 방법은 어떤 다른 게임 요소에도 적용될 수 있나요?

5. **볼과 패들의 상호작용**: `BALL` 객체의 움직임이 `PADDLE`과 어떻게 상호작용할 수 있을지 예상해보세요. 볼이 패들이나 블록에 부딪혔을 때의 반응을 프로그래밍하기 위해 어떤 추가적인 코드가 필요할까요?

6. **게임 루프 내에서의 객체 업데이트**: 게임 루프 내에서 `BALL.move()`와 `BALL.draw()`를 호출하는 과정이 게임의 흐름에 어떻게 기여하나요? 이러한 업데이트 메커니즘이 게임의 동적 요소를 관리하는 데 어떤 이점을 제공하나요?

이 질문들은 학습자가 게임 개발에서 객체의 움직임을 구현하고, 다양한 그래픽 요소를 효과적으로 표현하는 방법을 이해하는 데 도움을 줍니다. 또한, 게임 내 객체 간의 상호작용과 게임 루프의 역할에 대한 이해를 심화시킬 수 있습니다.
'''