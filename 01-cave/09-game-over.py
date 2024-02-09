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
    game_over = False  #############################################

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

        edge = holes[-1].copy()
        test = edge.move(0, slope)
        if test.top <= 0 or test.bottom >= 600:
            slope = randint(1, 6) * (-1 if slope > 0 else 1)
            edge.inflate_ip(0, -20)

        edge.move_ip(10, slope)
        holes.append(edge)

        del holes[0]
        holes = [x.move(-10, 0) for x in holes]

        ##############################################################
        if holes[0].top > ship_y or \
                holes[0].bottom < ship_y + 80:
            game_over = True  ########################################
        # 게임오버인지 확인하려면 아래 코드를 넣어 보세요.
        # print('game_over:', game_over)
        ##############################################################

        '''Rendering'''
        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()

'''

1. **게임 오버 조건**: `game_over` 변수를 사용하는 조건문은 어떤 상황에서 `True`가 되나요? 이 조건이 의미하는 바는 무엇이며, 게임 플레이에 어떤 영향을 미치나요?

2. **장애물과 충돌 감지**: `if holes[0].top > ship_y or holes[0].bottom < ship_y + 80:` 조건문을 통해 어떤 상황을 감지하려고 하는지 설명해주세요. 여기서 `ship_y + 80`은 어떤 값을 의미하며, 왜 이러한 조건을 사용했나요?

3. **게임 오버 로직의 실행 결과**: 코드에서 `game_over` 변수의 상태를 출력(`print('game_over:', game_over)`)하는 이유는 무엇인가요? 이러한 디버깅 방식이 개발 과정에서 어떻게 도움이 되나요?

충돌 감지, 게임 상태 관리, 조건문의 사용 등의 중요한 개념을 이해하는 데 도움을 줍니다. 또한, 게임 오버와 같은 핵심 게임 메커니즘을 구현하는 방법에 대한 인사이트를 제공할 수 있습니다.
'''