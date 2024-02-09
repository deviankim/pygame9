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
        test = edge.move(0, slope)                                  ###
        if test.top <= 0 or test.bottom >= 600:                     ###
            slope = randint(1, 6) * (-1 if slope > 0 else 1)    ###

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

1. **경사 조정과 경계 검사**: `edge.move(0, slope)`와 연관된 조건문을 사용하여 경사값의 방향을 변경하는 로직은 어떻게 작동하나요? `test.top <= 0 or test.bottom >= 600` 조건은 화면의 어떤 상황을 체크하며, 이 조건이 만족할 때 `slope` 값의 변화는 어떤 결과를 초래하나요?

2. **장애물의 이동과 업데이트**: `edge.move_ip(10, slope)`를 사용하여 장애물을 이동시키는 과정은 어떤 변화를 일으키나요? 이 코드가 각 프레임마다 실행됨으로써 게임 환경에 어떤 동적 변화를 추가하나요?

3. **장애물 리스트의 관리**: `del holes[0]`와 `holes = [x.move(-10, 0) for x in holes]` 구문은 각각 어떤 역할을 하며, 왜 이런 방식으로 장애물 리스트를 업데이트하나요? 이 코드를 통해 화면상의 장애물이 어떻게 유지되며, `holes` 리스트의 길이는 어떻게 조정되나요?

학습자가 게임 내에서 동적 요소를 생성하고 관리하는 방법, 조건에 따른 변수 값의 변경, 그리고 리스트와 객체의 속성을 활용하여 게임 환경을 업데이트하는 방법을 이해하는 데 도움을 줍니다. 또한, 게임 개발에 있어서 물리적인 요소(여기서는 경사)와 객체의 이동을 시뮬레이션하는 방법에 대한 이해를 심화시킬 수 있습니다.
'''