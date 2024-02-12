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

        if PADDLE.rect.colliderect(BALL.rect):  ######
            BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 80  #

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

1. **패들과 볼의 충돌 감지**: `PADDLE.rect.colliderect(BALL.rect)` 사용으로 패들과 볼의 충돌을 어떻게 감지하나요? 이 메서드가 반환하는 값은 무엇을 의미하며, 이를 통해 게임 로직에 어떻게 반응하게 만들 수 있나요?

2. **볼의 반사 각도 계산**: 볼이 패들에 충돌했을 때, `BALL.dir`의 값을 어떻게 계산하고 있나요? `(PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 80` 공식은 실제 물리학에서의 반사 각도 계산과 어떻게 관련이 있나요?

3. **게임 물리의 시뮬레이션**: 볼의 방향 변경 로직이 게임 내에서 물리적 상호작용을 어떻게 모방하고 있나요? 이 방식의 계산이 실제 핑퐁 게임의 볼 반사와 비슷한 효과를 내는 원리에 대해 설명해보세요.

4. **조건부 로직의 게임 내 적용**: 볼이 패들에 부딪힌 후 방향을 바꾸는 로직을 게임에 어떻게 통합했나요? 이 조건부 로직이 게임 플레이에 어떤 영향을 미치며, 플레이어의 경험을 어떻게 향상시키나요?

5. **패들의 위치에 따른 볼의 반사**: 패들의 중심과 볼의 중심 위치의 차이가 볼의 반사 각도에 어떻게 영향을 미치나요? 패들을 움직여 볼의 반사 각도를 조절하는 메커니즘이 게임 전략에 어떤 추가적인 깊이를 더하나요?

6. **게임 디자인과 사용자 인터페이스**: 볼과 패들의 상호작용을 통해 사용자는 게임 내에서 어떤 결정을 내릴 수 있나요? 이러한 게임 메커니즘이 사용자의 의사결정 과정과 게임의 재미에 어떤 영향을 미치는지 논의해 보세요.

이 질문들은 학습자가 게임 개발에서의 충돌 감지, 물리 시뮬레이션, 조건부 로직의 적용, 그리고 사용자 인터페이스 디자인의 중요성에 대해 깊이 이해하는 데 도움을 줍니다.
'''