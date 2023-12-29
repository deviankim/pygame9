import sys
from math import sqrt
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_a, K_RIGHT, K_d, K_DOWN, K_s, K_UP, K_w, K_SPACE

block_data = (
    (
        (0, 0, 1, \
         1, 1, 1, \
         0, 0, 0),
        (0, 1, 0, \
         0, 1, 0, \
         0, 1, 1),
        (0, 0, 0, \
         1, 1, 1, \
         1, 0, 0),
        (1, 1, 0, \
         0, 1, 0, \
         0, 1, 0),
    ), (
        (2, 0, 0, \
         2, 2, 2, \
         0, 0, 0),
        (0, 2, 2, \
         0, 2, 0, \
         0, 2, 0),
        (0, 0, 0, \
         2, 2, 2, \
         0, 0, 2),
        (0, 2, 0, \
         0, 2, 0, \
         2, 2, 0)
    ), (
        (0, 3, 0, \
         3, 3, 3, \
         0, 0, 0),
        (0, 3, 0, \
         0, 3, 3, \
         0, 3, 0),
        (0, 0, 0, \
         3, 3, 3, \
         0, 3, 0),
        (0, 3, 0, \
         3, 3, 0, \
         0, 3, 0)
    ), (
        (4, 4, 0, \
         0, 4, 4, \
         0, 0, 0),
        (0, 0, 4, \
         0, 4, 4, \
         0, 4, 0),
        (0, 0, 0, \
         4, 4, 0, \
         0, 4, 4),
        (0, 4, 0, \
         4, 4, 0, \
         4, 0, 0)
    ), (
        (0, 5, 5, \
         5, 5, 0, \
         0, 0, 0),
        (0, 5, 0, \
         0, 5, 5, \
         0, 0, 5),
        (0, 0, 0, \
         0, 5, 5, \
         5, 5, 0),
        (5, 0, 0, \
         5, 5, 0, \
         0, 5, 0)
    ), (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6)
    ), (
        (0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0),
        (0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0)
    )
)


class Block:
    def __init__(self, count):
        self.turn = randint(0, 3)
        self.type = block_data[randint(0, 6)]
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.xpos = randint(2, 8 - self.size)
        self.ypos = 1 - self.size
        self.fire = count + interval

    def update(self, count):
        erased = 0
        if is_overlapped(self.xpos, self.ypos + 1, self.turn):
            for y_offset in range(block.size):
                for x_offset in range(block.size):
                    if 0 <= self.xpos + x_offset < width and 0 <= self.ypos + y_offset < height:
                        value = block.data[y_offset * block.size + x_offset]

                        if value != 0:
                            field[self.ypos + y_offset][self.xpos + x_offset] = value
            erased = erase_line()
            go_next_block(count)
        if self.fire < count:
            self.fire = count + interval
            self.ypos += 1

        return erased

    def draw(self):
        for index in range(len(self.data)):
            xpos = index % self.size
            ypos = int(index / self.size)
            value = self.data[index]
            if 0 <= ypos + self.ypos < height and 0 <= xpos < width and value != 0:
                x_pos = 25 + (xpos + self.xpos) * 25
                y_pos = 25 + (ypos + self.ypos) * 25
                pygame.draw.rect(surface, colors[value], (x_pos, y_pos, 24, 24))


def erase_line():
    erased = 0
    ypos = 20
    while ypos >= 0:
        if all(field[ypos]):
            erased += 1
            del field[ypos]
            field.insert(0, [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
        else:
            ypos -= 1
    return erased


def is_game_over():
    filled = 0
    for cell in field[0]:
        if cell != 0:
            filled += 1
    return filled > 2


def go_next_block(count):
    global block, next_block
    block = next_block if next_block is not None else Block(count)
    next_block = Block(count)


def is_overlapped(xpos, ypos, turn):
    data = block.type[turn]
    for y_offset in range(block.size):
        for x_offset in range(block.size):
            if 0 <= xpos + x_offset < width and 0 <= ypos + y_offset < height:
                if data[y_offset * block.size + x_offset] != 0 and field[ypos + y_offset][xpos + x_offset] != 0:
                    return True
    return False


pygame.init()
pygame.key.set_repeat(30, 30)
surface = pygame.display.set_mode([600, 600])
fpsclock = pygame.time.Clock()
width = 12
height = 22
interval = 40
field = [[0 for _ in range(width)] for _ in range(height)]
colors = ((0, 0, 0), (255, 165, 0), (0, 0, 255),
          (0, 255, 255), (0, 255, 0), (255, 0, 255),
          (255, 255, 0), (255, 0, 0), (128, 128, 128))
block = None
next_block = None


def main():
    global interval
    count = 0
    score = 0
    game_over = False
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_over = largefont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (300, 300)

    go_next_block(interval)

    for ypos in range(height):
        for xpos in range(width):
            field[ypos][xpos] = 8 if xpos == 0 or xpos == width - 1 else 0

    for index in range(width):
        field[height - 1][index] = 8

    while True:
        key = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        game_over = is_game_over()

        if not game_over:
            count += 5
            if count % 1000 == 0:
                interval = max(1, interval - 2)
            erased = block.update(count)

            if erased > 0:
                score += (2 ** erased) * 100

            next_x, next_y, next_t = block.xpos, block.ypos, block.turn
            if key in [K_SPACE, K_w, K_UP]:
                next_t = (next_t + 1) % 4
            elif key in [K_RIGHT, K_d]:
                next_x += 1
            elif key in [K_LEFT, K_a]:
                next_x -= 1
            elif key in [K_DOWN, K_s]:
                next_y += 1

            if not is_overlapped(next_x, next_y, next_t):
                block.xpos = next_x
                block.ypos = next_y
                block.turn = next_t
                block.data = block.type[block.turn]

        surface.fill((0, 0, 0))
        for ypos in range(height):
            for xpos in range(width):
                value = field[ypos][xpos]
                pygame.draw.rect(surface, colors[value], (xpos * 25 + 25, ypos * 25 + 25, 24, 24))
        block.draw()

        for ypos in range(next_block.size):
            for xpos in range(next_block.size):
                value = next_block.data[xpos + ypos * next_block.size]
                pygame.draw.rect(surface, colors[value], (xpos * 25 + 460, ypos * 25 + 100, 24, 24))

        score_str = str(score).zfill(6)
        score_image = smallfont.render(score_str, True, (0, 255, 0))
        surface.blit(score_image, (500, 30))

        if game_over:
            surface.blit(message_over, message_rect)

        pygame.display.update()
        fpsclock.tick(15)


if __name__ == '__main__':
    main()
