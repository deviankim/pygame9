import sys

import pygame
from pygame.locals import QUIT, KEYDOWN, Rect, K_q, K_f, KEYUP

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
    slope = 50

    holes = []
    for i in range(walls):
        holes.append(Rect(i * hole_width, 100, hole_width, 400))

    while True:

        process_event_queue()

        clear_screen()

        draw_holes(holes)
        update_screen(1)
        edge = holes[-1].copy()
        draw_hole(color_gray, edge)
        update_screen(1)
        test = edge.move(0, slope)
        draw_hole(color_hole, edge)
        draw_hole(color_yellow, test)
        update_screen(1)
        clear_screen()
        draw_holes(holes)

        if test.top <= 0 or test.bottom >= 600:
            slope *= -1
            edge.move_ip(hole_width, slope)
            draw_hole(color_yellow, edge)
            update_screen(1)
            edge.inflate_ip(0, -20)
            draw_hole(color_red, edge)
            update_screen(1)
            clear_screen()
        else:
            edge.move_ip(hole_width, slope)
            draw_hole(color_yellow, edge)
            update_screen(1)

        holes.append(edge)

        draw_holes(holes)
        update_screen(1)

        # draw hole to be deleted
        front = holes[0]
        draw_hole(color_red, front)
        update_screen(1)

        draw_hole(color_bg, front)
        update_screen(1)

        del holes[0]
        draw_holes(holes)
        update_screen(1)

        holes = [hole.move(-hole_width, 0) for hole in holes]


def clear_screen():
    SURFACE.fill(color_bg)


def draw_hole(color, rect):
    pygame.draw.rect(SURFACE, (255, 255, 255), rect.inflate(+2, +2))
    pygame.draw.rect(SURFACE, color, rect.inflate(-2, -2))


def draw_holes(holes):
    for hole in holes:
        draw_hole(color_hole, hole)


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
