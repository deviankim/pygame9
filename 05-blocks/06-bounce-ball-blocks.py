import math
import random
import sys

import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT


class Block:
    def __init__(self, color, rect, speed=0):
        self.color = color
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.color, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.color, self.rect)


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10)


def main():
    global BLOCKS
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
        if BALL.rect.centery < 1000:
            BALL.move()

        prev_len = len(BLOCKS)                              #
        BLOCKS = [x for x in BLOCKS                         #
                  if not x.rect.colliderect(BALL.rect)]     #
        if len(BLOCKS) != prev_len:                         #
            BALL.dir *= -1                                  #

        if PADDLE.rect.colliderect(BALL.rect):
            BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 80

        SURFACE.fill((0, 0, 0))
        BALL.draw()
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

1. **블록과 볼의 충돌 처리**: `BLOCKS = [x for x in BLOCKS if not x.rect.colliderect(BALL.rect)]` 이 코드는 어떤 작업을 수행하나요? 이 코드가 블록과 볼의 충돌을 어떻게 감지하고 처리하는지 설명해주세요.

2. **충돌 시의 동작 변경**: `if len(BLOCKS) != prev_len: BALL.dir *= -1` 이 조건문은 무엇을 체크하고, 충돌이 감지되었을 때 볼의 방향은 어떻게 변경되나요? 이 로직이 게임 플레이에 어떤 영향을 미치는지 설명해보세요.

3. **리스트 컴프리헨션의 활용**: 리스트 컴프리헨션을 사용하여 충돌한 블록을 `BLOCKS` 리스트에서 제거하는 방식은 어떤 장점이 있나요? 이 방식이 코드의 가독성과 성능에 어떤 영향을 미칠 수 있나요?

4. **게임 물리와 반응**: 블록과 충돌 후 볼의 방향이 반대로 바뀌는 것은 실제 물리 법칙과 어떻게 비교될 수 있나요? 이러한 게임 내 물리 시뮬레이션이 사용자 경험에 어떤 영향을 줄 수 있나요?

5. **게임의 동적 요소 관리**: 충돌 감지 및 처리 로직을 통해 게임의 동적 요소를 어떻게 관리하고 있나요? 이러한 방식이 게임의 상태를 업데이트하고 유지하는 데 어떤 역할을 하는지 논의해보세요.

6. **게임 개발에서의 조건문 활용**: 충돌 감지 후 처리를 위한 조건문의 사용은 게임 개발에서 어떤 중요한 개념을 나타내나요? 조건문을 통한 게임 로직의 분기 처리가 게임 디자인에 어떤 유연성을 제공하는지 설명해보세요.

이 질문들은 학습자가 충돌 처리, 게임 물리의 시뮬레이션, 그리고 동적 게임 요소의 관리에 대한 이해를 심화하는 데 도움을 줍니다. 또한, 게임 개발 과정에서 조건문과 리스트 컴프리헨션과 같은 프로그래밍 기법의 적용 방법에 대해서도 더 잘 이해할 수 있게 됩니다.
'''