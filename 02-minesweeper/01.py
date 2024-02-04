import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((300, 200))
FPSCLOCK = pygame.time.Clock()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()

###
'''
1. `pygame.init()` 함수의 목적은 무엇인가요?
2. `pygame.display.set_mode((300, 200))`에서 `(300, 200)`은 어떤 의미를 가지나요?
3. `FPSCLOCK.tick(15)`에서 `15`는 무엇을 의미하고, 이 값을 변경하면 어떤 영향을 미치나요?
'''