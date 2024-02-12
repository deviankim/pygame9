import sys

import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT


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
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))


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

        SURFACE.fill((0, 0, 0))
        PADDLE.draw()
        for block in BLOCKS:
            block.draw()

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
