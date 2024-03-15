import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_a, K_s, K_d

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    # initialize
    game_over = False
    score = 0
    speed = 25
    rocks = []
    keymap = []
    ship_x, ship_y = (0, 0)
    scope_image = pygame.image.load("scope.png")
    rock_image = pygame.image.load("rock.png")

    scorefont = pygame.font.SysFont(None, 36)
    sysfont = pygame.font.SysFont(None, 72)
    message_over = sysfont.render("GAME OVER!!!", True, (0, 255, 255))
    message_rect = message_over.get_rect()
    message_rect.center = (800 / 2, 800 / 2)

    pygame.mixer.music.load("Escape.mp3")
    pygame.mixer.music.play()

    while len(rocks) < 200:
        rocks.append({
            "pos": [randint(-1600, 1600), randint(-1600, 1600), randint(0, 4095)],
            "theta": randint(0, 360)
        })

    while True:
        # update key
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key not in keymap:
                    keymap.append(event.key)
            elif event.type == KEYUP:
                keymap.remove(event.key)

        # process frames
        if not game_over:
            score += 1
            if score % 10 == 0:
                speed += 1
            if K_a in keymap or K_LEFT in keymap:
                ship_x -= 30
            elif K_d in keymap or K_RIGHT in keymap:
                ship_x += 30
            elif K_UP in keymap or K_w in keymap:
                ship_y -= 30
            elif K_s in keymap or K_DOWN in keymap:
                ship_y += 30

            ship_x = max(-800, min(800, ship_x))
            ship_y = max(-800, min(800, ship_y))

            for rock in rocks:
                rock["pos"][2] -= speed
                if rock["pos"][2] < 64:
                    if abs(rock["pos"][0] - ship_x) < 50 and \
                            abs(rock["pos"][1] - ship_y) < 50:
                        game_over = True
                    rock["pos"] = [randint(-1600, 1600), randint(-1600, 1600), 4095]

        # render
        SURFACE.fill((0, 0, 0))

        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - ship_x) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - ship_y) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        SURFACE.blit(scope_image, (0, 0))

        if game_over:
            SURFACE.blit(message_over, message_rect)
            pygame.mixer.music.stop()

        # render score
        score_str = str(score).zfill(6)
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        SURFACE.blit(score_image, (700, 50))

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == "__main__":
    main()

'''
1. 방향키 상하 반대로 적용 하기

'''