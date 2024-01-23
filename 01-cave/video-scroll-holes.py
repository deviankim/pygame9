import sys
from random import randint

import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect, K_q, K_f, KEYUP

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((830, 600))

FPSCLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)

color_bg = (0, 255, 0)
color_hole = (0, 0, 0)
color_bg_coordinates = (128, 128, 128)
color_coordinates = (255, 255, 255)
color_red = (255, 0, 0)
color_gray = (128, 128, 128)
color_yellow = (255, 255, 0)
walls = 8
hole_width = 100
ff = False


def main():
    ship_y = 250
    velocity = 0
    ship_image = pygame.image.load("ship.png")
    slope = 20

    holes = []
    for i in range(walls):
        holes.append(Rect(i * hole_width, 100, hole_width, 400))

    while True:

        process_event_queue()

        SURFACE.fill(color_bg)

        draw_holes(holes)

        update_screen(1)
        edge = holes[-1].copy()
        pygame.draw.rect(SURFACE, color_gray, edge)
        update_screen(1) # 테스트 샘플
        test = edge.move(0, slope)
        pygame.draw.rect(SURFACE, color_hole, edge)
        pygame.draw.rect(SURFACE, color_yellow, test)
        update_screen(1) # 테스트
        pygame.draw.rect(SURFACE, color_bg, test)
        pygame.draw.rect(SURFACE, color_hole, edge)

        if test.top <= 0 or test.bottom >= 600:
            slope *= -1
            edge.inflate_ip(0, -20)  # 동굴 높이를 20씩 줄이기

        edge.move_ip(hole_width, slope)
        holes.append(edge)

        pygame.draw.rect(SURFACE, color_yellow, edge)
        update_screen(1)

        draw_holes(holes)
        update_screen(1)

        # draw hole to be deleted
        front = holes[0]
        pygame.draw.rect(SURFACE, color_red, front)
        update_screen(1)

        pygame.draw.rect(SURFACE, color_bg, front)
        update_screen(1)

        count = 0
        slow_before = 2
        del holes[0]
        for hole in holes:
            pygame.draw.rect(SURFACE, color_yellow, hole)
            update_screen(5 if count < slow_before else 30)
            pygame.draw.rect(SURFACE, color_bg, hole)
            hole.move_ip(-hole_width, 0)
            pygame.draw.rect(SURFACE, color_yellow, hole)
            update_screen(5 if count < slow_before else 30)
            pygame.draw.rect(SURFACE, color_hole, hole)
            update_screen(5 if count < slow_before else 30)
            count += 1

        update_screen(1)


def draw_holes(holes):
    for hole in holes:
        pygame.draw.rect(SURFACE, color_hole, hole)


def update_screen(fps=1):
    pygame.display.update()
    FPSCLOCK.tick(30 if ff else fps)


def process_event_queue():
    global ff
    for event in pygame.event.get():
        if event.type == QUIT:
            quit_game()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                quit_game()
            elif event.key == K_f:
                ff = True
        elif event.type == KEYUP:
            if event.key == K_f:
                ff = False


def quit_game():
    pygame.quit()
    sys.exit()


main()
