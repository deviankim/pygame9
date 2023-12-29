import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
from pygame.time import Clock

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK: Clock = pygame.time.Clock()


def main():
    """Main Routine"""

    # initialize variables
    walls = 80
    ship_y = 250
    velocity = -25
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")

    ship_height = ship_image.get_height()

    # setup holes
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))
    game_over = False

    while True:
        is_space_down = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                is_space_down = True

        # move my ship
        if not game_over:
            score += 10
            velocity += -3 if is_space_down else 3

            ship_y += velocity

            # 동굴을 스크롤
            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0, -20)
            edge.move_ip(10, slope)
            holes.append(edge)
            del holes[0]
            holes = [x.move(-10, 0) for x in holes]

            # intersect?
            if ship_y < holes[0].top or holes[0].bottom < ship_y + ship_height:
                game_over = True

        # render
        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render(f"score is {score}", True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20))
        score_image = sysfont.render(f"velocity: {velocity}", True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 40))
        score_image = sysfont.render(f"ship_y: {ship_y}", True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 60))

        if game_over:
            SURFACE.blit(bang_image, (0 + ship_image.get_width() / 2 - bang_image.get_width() / 2,
                                      ship_y + ship_image.get_height() / 2 - bang_image.get_height() / 2))

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()


"""
- 필수 준비:
  [] 단계별로 쪼개서 실행 세트 만들기
  [] 숙제 리스트 만들기

- TODO:
  [] 게임오버시 엔터 누르면 게임 재시작
  [] 
"""