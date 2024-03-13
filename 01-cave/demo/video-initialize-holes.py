import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect, K_q

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))

FPSCLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)

color_bg = (0, 255, 0)
color_hole = (0, 0, 0)
color_bg_coordinates = (128, 128, 128)
color_coordinates = (255, 255, 255)


def main():
    walls = 80
    ship_y = 250
    velocity = 0
    ship_image = pygame.image.load("ship.png")

    holes = []

    SURFACE.fill(color_bg)

    for i in range(walls):
        x = i * 10
        y = 100
        holes.append(Rect(x, y, 10, 400))

        process_event_queue()

        hole = holes[-1]
        pygame.draw.rect(SURFACE, (80, 80, 80), hole)

        index_image = sysfont.render(f"[{i}] x:{x}, y:{y}", True, color_coordinates)
        index_rect = index_image.get_rect()
        index_rect.move_ip(x + 20, y)

        pygame.draw.rect(SURFACE, color_bg_coordinates, index_rect)
        SURFACE.blit(index_image, index_rect)
        pygame.display.update()
        FPSCLOCK.tick(1)
        pygame.draw.rect(SURFACE, color_bg, index_rect)
        pygame.draw.rect(SURFACE, color_hole, hole)


def process_event_queue():
    for event in pygame.event.get():
        if event.type == QUIT:
            quit_game()
        elif event.type == KEYDOWN and event.key == K_q:
            quit_game()


def quit_game():
    pygame.quit()
    sys.exit()


main()
