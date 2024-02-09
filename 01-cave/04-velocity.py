import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    ship_y = 0                                      ###
    velocity = 0                                    ###
    ship_image = pygame.image.load("ship.png")

    while True:

        '''InputEvent'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        '''Update'''
        velocity += 3                               ###
        ship_y += velocity                          ###

        '''Rendering'''
        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, ship_y))   ###

        pygame.display.update()

        FPSCLOCK.tick(15)


main()

'''

1. **변수의 역할과 변화**: `ship_y`와 `velocity` 변수는 프로그램 내에서 어떤 역할을 합니다? 이 변수들이 각 프레임마다 어떻게 변화하며, 이러한 변화가 게임의 실행에 어떤 영향을 미치나요?

2. **이미지의 움직임 구현**: `velocity += 3`와 `ship_y += velocity` 구문을 통해 이미지의 움직임을 어떻게 구현했나요? 이 로직이 `while True:` 루프 안에서 실행될 때, 화면에 나타나는 이미지의 움직임은 어떻게 변화하나요?

3. **화면 업데이트와 프레임 속도**: `SURFACE.blit(ship_image, (0, ship_y))` 구문은 어떤 작업을 수행하나요? `ship_y`의 값이 변할 때마다 이미지의 위치는 어떻게 달라지며, `FPSCLOCK.tick(15)` 호출이 이 움직임에 어떤 영향을 미치나요?

'''