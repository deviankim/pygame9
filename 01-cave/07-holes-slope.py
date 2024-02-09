import sys
from random import randint  ##########################
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
    slope = randint(1, 6)  ##########################
    ship_image = pygame.image.load("ship.png")

    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))

    while True:
        is_space_down = False

        '''InputEvent'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                is_space_down = True

        '''Update'''
        velocity += -3 if is_space_down else 3
        ship_y += velocity

        edge = holes[-1].copy()                     ###

        edge.move_ip(10, slope)                     ###
        holes.append(edge)                          ###

        del holes[0]                                ###
        holes = [x.move(-10, 0) for x in holes]     ###

        '''Rendering'''
        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **랜덤 함수의 활용**: `randint(1, 6)` 함수의 사용 목적은 무엇인가요? 이 함수가 게임의 어떤 요소에 영향을 미치며, 게임 플레이에 어떤 다양성을 추가하나요?

2. **장애물의 이동 구현**: `edge.move_ip(10, slope)`와 `holes = [x.move(-10, 0) for x in holes]` 코드는 게임 화면에서 장애물이 어떻게 움직이는지를 결정합니다. 이 코드가 구현하는 시각적 효과는 무엇이며, 게임 플레이에 어떤 영향을 미치나요?

3. **게임 환경의 변화**: 장애물을 지속적으로 새로 추가하고 오래된 장애물을 제거(`del holes[0]`)하는 과정은 게임 환경에 어떤 지속적인 변화를 가져오나요? 이러한 변화가 게임의 재미를 유지하는 데 어떻게 기여하나요?

랜덤 함수의 활용, 동적 장애물 생성 및 관리, 사용자 입력 처리, 그리고 게임 물리의 기본 개념을 이해하는 데 도움을 줍니다. 또한, 게임 디자인에서 플레이어에게 지속적으로 새로운 도전을 제공하고 게임의 재미를 유지하는 방법에 대한 인사이트를 제공할 수 있습니다.
'''