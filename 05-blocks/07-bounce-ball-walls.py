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

        prev_len = len(BLOCKS)
        BLOCKS = [x for x in BLOCKS
                  if not x.rect.colliderect(BALL.rect)]
        if len(BLOCKS) != prev_len:
            BALL.dir *= -1

        if PADDLE.rect.colliderect(BALL.rect):
            BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 80

        if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:    #
            BALL.dir = 180 - BALL.dir                           #
        if BALL.rect.centery < 0:                               #
            BALL.dir = -BALL.dir                                #
            BALL.speed = 15                                     #

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

1. **볼의 경계 처리**: 볼이 화면의 왼쪽이나 오른쪽 경계에 닿았을 때 `BALL.dir = 180 - BALL.dir`를 통해 볼의 방향을 어떻게 조정하나요? 이 로직이 실제 물리적 반사와 어떻게 유사한가요?

2. **볼의 상단 경계 처리**: 볼이 화면의 상단 경계에 닿았을 때 `BALL.dir = -BALL.dir`와 `BALL.speed = 15`를 통해 어떤 변화를 주고 있나요? 이 변화가 게임 플레이에 어떤 영향을 미치며, 왜 볼의 속도를 변경하나요?

3. **속도와 방향의 동적 조정**: 볼의 속도(`BALL.speed`)와 방향(`BALL.dir`)을 동적으로 조정하는 것이 게임에 어떤 다양성과 도전을 추가하나요? 이러한 메커니즘이 게임의 재미 요소에 어떤 역할을 하나요?

4. **충돌 반응의 물리적 정확성**: 코드에서 사용된 볼의 반사 각도 계산이 실제 물리 법칙을 어떻게 반영하고 있나요? 게임 개발에서 물리 법칙을 정확히 모방하는 것의 중요성에 대해 설명해보세요.

5. **게임 내 오브젝트의 상호작용**: 볼과 패들 또는 벽의 충돌을 처리하는 로직이 게임 내 다양한 오브젝트 간의 상호작용을 구현하는 데 어떻게 기여하나요? 이러한 상호작용이 게임의 동적 환경을 만드는 데 어떤 역할을 하나요?

6. **게임 난이도 조절**: 볼의 속도를 증가시키는 것이 게임의 난이도에 어떤 영향을 미치나요? 게임 개발에서 난이도 조절의 중요성과 난이도를 조절하는 다양한 방법에 대해 논의해보세요.

이 질문들은 학습자가 게임 개발 과정에서 충돌 처리, 물리 시뮬레이션, 게임 내 객체의 상호작용, 그리고 게임의 난이도 조절 등의 개념을 이해하고 적용하는 데 도움을 줄 수 있습니다.
'''