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


def update():                                                   #
    global BLOCKS                                               #
    for event in pygame.event.get():                            #
        if event.type == QUIT:                                  #
            pygame.quit()                                       #
            sys.exit()                                          #
        elif event.type == KEYDOWN:                             #
            if event.key == K_LEFT:                             #
                PADDLE.rect.centerx -= 10                       #
            elif event.key == K_RIGHT:                          #
                PADDLE.rect.centerx += 10                       #
    if BALL.rect.centery < 1000:                                #
        BALL.move()                                             #
    prev_len = len(BLOCKS)                                      #
    BLOCKS = [x for x in BLOCKS                                 #
              if not x.rect.colliderect(BALL.rect)]             #
    if len(BLOCKS) != prev_len:                                 #
        BALL.dir *= -1                                          #
    if PADDLE.rect.colliderect(BALL.rect):                      #
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 80      #
    if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:        #
        BALL.dir = 180 - BALL.dir                               #
    if BALL.rect.centery < 0:                                   #
        BALL.dir = -BALL.dir                                    #
        BALL.speed = 15                                         #


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10)


def main():
    global BLOCKS
    myfont = pygame.font.SysFont(None, 80)
    message_clear = myfont.render("Cleared!", True, (255, 255, 0))
    message_over = myfont.render("Game Over!", True, (255, 255, 0))
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color=color, rect=Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))

    while True:
        update()                                    ##################

        SURFACE.fill((0, 0, 0))
        BALL.draw()
        PADDLE.draw()
        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            SURFACE.blit(message_clear, (200, 400))
        if BALL.rect.centery > 800 and len(BLOCKS) > 0:
            SURFACE.blit(message_over, (150, 400))

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
'주석이 붙은 코드는 새로 추가된 코드야. 새로 추가된 코드를 위주로 교육용 질문을 몇 개 만들어 줘'

'''
새로 추가된 코드를 중심으로 만들 수 있는 교육용 질문은 다음과 같습니다:

1. **게임 논리와 이벤트 처리 분리**: `update()` 함수에서 이벤트 처리와 게임 논리를 분리하는 이유는 무엇인가요? 이러한 구조가 게임 개발에 어떤 이점을 제공하나요?

2. **함수로 로직 분리의 중요성**: `update()` 함수를 통해 게임 로직을 분리하는 것이 코드의 가독성과 유지 보수성에 어떤 이점을 제공하나요? 함수를 사용하여 코드를 구조화하는 것의 중요성에 대해 설명해주세요.

이 질문들은 학습자가 게임 개발 과정에서 중요한 개념과 기술을 이해하고 적용하는 데 도움을 줄 수 있습니다.
'''