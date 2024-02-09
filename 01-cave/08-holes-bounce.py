import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    walls = 80
    ship_y = 250
    velocity = 0
    slope = randint(1, 6)
    ship_image = pygame.image.load("ship.png")

    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))

    while True:
        is_space_down = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                is_space_down = True

        velocity += -3 if is_space_down else 3
        ship_y += velocity

        edge = holes[-1].copy()
        test = edge.move(0, slope)                              ###
        if test.top <= 0 or test.bottom >= 600:                 ###
            slope = randint(1, 6) * (-1 if slope > 0 else 1)    ###
            edge.inflate_ip(0, -20)                             ###

        edge.move_ip(10, slope)
        holes.append(edge)

        del holes[0]
        holes = [x.move(-10, 0) for x in holes]

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **장애물의 경계 조건 검사**: `test = edge.move(0, slope)`와 연결된 조건문을 통해 장애물이 화면의 상단 또는 하단 경계에 도달했을 때 어떤 처리가 이루어지나요? 이러한 경계 조건 검사가 게임 플레이에 어떻게 영향을 미치는지 설명해보세요.

2. **경사도 변경 로직**: `slope = randint(1, 6) * (-1 if slope > 0 else 1)` 코드를 통해 경사도가 어떻게 조정되며, 이것이 장애물의 움직임에 어떤 영향을 미치는지 설명할 수 있나요? 경사도를 무작위로 변경하는 이유는 무엇인가요?

3. **장애물 크기 조정**: `edge.inflate_ip(0, -20)` 코드는 장애물의 크기를 어떻게 조정하나요? 이러한 크기 조정이 게임의 도전적인 요소에 어떤 영향을 미치며, 플레이어에게 어떤 새로운 경험을 제공하나요?

물리적 동작, 무작위 요소의 사용, 그리고 동적인 게임 환경 구성의 중요성을 이해하는 데 도움을 줍니다. 또한, 이러한 요소들이 게임의 재미와 도전적인 면을 어떻게 증진시키는지에 대한 통찰력을 제공할 수 있습니다.

'''