import sys
from random import randint
import pygame
from pygame.locals import Rect, QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d

pygame.init()
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode((600, 600))
fpsclock = pygame.time.Clock()


class Drawable:
    def __init__(self, rect, offset0, offset1):
        strip = pygame.image.load("strip.png")
        self.images = (pygame.Surface((24, 24), pygame.SRCALPHA),
                       pygame.Surface((24, 24), pygame.SRCALPHA))
        self.rect = rect
        self.count = 0
        self.images[0].blit(strip, (0, 0), Rect(offset0, 0, 24, 24))
        self.images[1].blit(strip, (0, 0), Rect(offset1, 0, 24, 24))

    def move(self, diff_x, diff_y):
        self.count += 1
        self.rect.move_ip(diff_x, diff_y)

    def draw(self):
        image = self.images[0] if self.count % 2 == 0 else self.images[1]
        surface.blit(image, self.rect.topleft)


class Ship(Drawable):
    def __init__(self):
        super().__init__(Rect(300, 550, 24, 24), 192, 192)


class Beam(Drawable):
    def __init__(self):
        super().__init__(Rect(300, 0, 24, 24), 0, 24)


class Bomb(Drawable):
    def __init__(self):
        super().__init__(Rect(300, -50, 24, 24), 48, 72)
        self.time = randint(5, 220)


class Alien(Drawable):
    def __init__(self, rect, offset, score):
        super().__init__(rect, offset, offset + 24)
        self.score = score


def main():
    sysfont = pygame.font.SysFont(None, 72)
    scorefont = pygame.font.SysFont(None, 36)
    message_clear = sysfont.render("CLEARED", True, (0, 255, 225))
    message_over = sysfont.render("Game over", True, (0, 255, 225))
    message_rect = message_clear.get_rect()
    message_rect.center = (300, 300)
    game_over = False
    moving_left = True
    moving_down = False
    move_interval = 20
    counter = 0
    score = 0
    aliens = []
    bombs = []
    ship = Ship()
    beam = Beam()

    for ypos in range(4):
        offset = 96 if ypos < 2 else 144
        for xpos in range(10):
            rect = Rect(100 + xpos * 50, ypos * 50 + 50, 24, 24)
            alien = Alien(rect, offset, (4 - ypos) * 10)
            aliens.append(alien)

    for _ in range(4):
        bombs.append(Bomb())

    while True:
        ship_move_x = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key in [K_LEFT, K_a]:
                    ship_move_x = -5
                elif event.key in [K_RIGHT, K_d]:
                    ship_move_x = 5
                elif event.key == K_SPACE and beam.rect.bottom < 0:
                    beam.rect.center = ship.rect.center

        if not game_over:
            counter += 1
            ship.move(ship_move_x, 0)

            beam.move(0, -15)

            area = aliens[0].rect.copy()
            for alien in aliens:
                area.union_ip(alien.rect)

            if counter % move_interval == 0:
                move_x = -5 if moving_left else 5
                move_y = 0

                if (area.left < 10 or area.right > 590) and not moving_down:
                    moving_left = not moving_left
                    move_x, move_y = 0, 24
                    move_interval = max(1, move_interval - 2)
                    moving_down = True
                else:
                    moving_down = False

                for alien in aliens:
                    alien.move(move_x, move_y)

            if area.bottom > 550:
                game_over = True

            for bomb in bombs:
                if bomb.time < counter and bomb.rect.top < 0:
                    enemy = aliens[randint(0, len(aliens) - 1)]
                    bomb.rect.center = enemy.rect.center

                if bomb.rect.top > 0:
                    bomb.move(0, 10)

                if bomb.rect.top > 600:
                    bomb.time += randint(50, 250)
                    bomb.rect.top = -50

                if bomb.rect.colliderect(ship.rect):
                    game_over = True

            # 빔과 외계인 충돌?
            tmp = []
            for alien in aliens:
                if alien.rect.collidepoint(beam.rect.center):
                    beam.rect.top = -50
                    score += alien.score
                else:
                    tmp.append(alien)
            aliens = tmp

            if len(aliens) == 0:
                game_over = True

        surface.fill((0, 0, 0))
        for alien in aliens:
            alien.draw()
        ship.draw()
        beam.draw()
        for bomb in bombs:
            bomb.draw()

        score_str = str(score).zfill(5)
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        surface.blit(score_image, (500, 10))

        if game_over:
            if len(aliens) == 0:
                surface.blit(message_clear, message_rect.topleft)
            else:
                surface.blit(message_over, message_rect.topleft)

        pygame.display.update()
        fpsclock.tick(20)


if __name__ == '__main__':
    main()
