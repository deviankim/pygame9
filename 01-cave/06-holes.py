import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect  ###

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))

FPSCLOCK = pygame.time.Clock()


def main():
    walls = 80                                              ###
    ship_y = 250
    velocity = 0
    ship_image = pygame.image.load("ship.png")

    holes = []                                              ###
    for xpos in range(walls):                               ###
        holes.append(Rect(xpos * 10, 100, 10, 400))     ###

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

        SURFACE.fill((0, 255, 0))

        for hole in holes:                                  ###
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)  ###

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **Rect 객체 사용**: `Rect` 객체를 사용하여 `holes` 리스트에 추가하는 과정에서 `Rect(xpos * 10, 100, 10, 400)` 구문이 어떤 값을 나타내며, `Rect` 객체를 생성하는 이유는 무엇인가요?

2. **장애물(구멍) 리스트 초기화**: `holes` 리스트를 초기화하는 과정에서 사용된 반복문(`for xpos in range(walls)`)은 어떤 작업을 수행하나요? 여기서 `walls` 변수는 어떤 역할을 하며, 왜 `holes` 리스트에 여러 개의 `Rect` 객체를 추가하나요?

3. **장애물(구멍) 그리기**: `for hole in holes:` 반복문을 사용하여 각 구멍을 화면에 그리는 과정(`pygame.draw.rect(SURFACE, (0, 0, 0), hole)`)은 어떻게 작동하나요? 각 `Rect` 객체는 화면에 어떻게 표현되며, 이러한 방식으로 장애물을 표현하는 것이 게임 플레이에 어떤 영향을 미치나요?

'''