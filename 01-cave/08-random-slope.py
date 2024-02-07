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
    slope = randint(1, 6)  ###
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
        test = edge.move(0, slope)
        if test.top <= 0 or test.bottom >= 600:
            slope = randint(1, 6) * (-1 if slope > 0 else 1)  ###

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

1. **경사값 초기화**: `slope = randint(1, 6)` 구문은 프로그램 시작 시 장애물의 초기 경사값을 어떻게 설정하나요? 이 때, `randint` 함수의 사용이 게임의 시작마다 어떤 변화를 가져오며, 게임 플레이에 어떤 영향을 미치나요?

2. **경사값 변경 로직**: 화면의 상단 또는 하단에 도달했을 때 경사값을 변경하는 코드 `slope = randint(1, 6) * (-1 if slope > 0 else 1)`는 구체적으로 어떤 작업을 수행하나요? 여기서 사용된 조건부 표현식이 경사값의 방향 변경에 어떻게 작용하며, 이로 인해 게임 환경에 어떤 동적 변화가 발생하나요?

3. **동적 장애물 생성과 관리**: 장애물의 경사가 변경될 때, `holes` 리스트에 추가되는 새 `Rect` 객체의 경사가 어떻게 조정되나요? 이 과정이 장애물의 모양과 게임 내 도전의 난이도에 어떻게 영향을 미치나요?

프로그램의 랜덤 요소를 활용한 동적 게임 환경 구성, 조건부 로직의 구현, 그리고 게임 요소의 동적 관리 방법을 이해하는 데 도움을 줍니다. 또한, 게임 디자인에서 랜덤성이 게임의 재미와 재플레이 가치에 어떤 영향을 미치는지에 대한 인사이트를 제공할 수 있습니다.
'''