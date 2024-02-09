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
    game_over = False

    while True:
        is_space_down = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                is_space_down = True

        if not game_over:  #######################
            # 여기서부터
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

            if holes[0].top > ship_y or \
                    holes[0].bottom < ship_y + 80:
                game_over = True
            # 여기까지 들여쓰기(탭)을 한다.

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **게임 오버 상태 관리**: `if not game_over:` 조건문을 추가한 이유는 무엇인가요? 이 조건문이 게임의 로직에 어떤 영향을 미치며, 게임 오버가 되었을 때 게임의 동작은 어떻게 변화하나요?

2. **조건문의 범위 조정**: 주석으로 표시된 "여기서부터"와 "여기까지" 사이의 코드 블록을 `if not game_over:` 조건문 안으로 들여쓰기 함으로써 어떤 변화를 기대할 수 있나요? 이 변경이 게임 플레이에 어떤 실질적인 차이를 만들어내나요?

3. **게임 플레이 제어 로직**: 게임 오버가 되었을 때, 플레이어의 조작에 대한 반응을 중지시키는 것이 게임 디자인 측면에서 왜 중요한가요? 이러한 디자인 결정이 사용자 경험에 어떤 영향을 미칠 수 있나요?

4. **게임 오버 후의 게임 상태**: 게임 오버가 되었을 때도 `SURFACE.fill`, `pygame.draw.rect`, `SURFACE.blit`, `pygame.display.update` 함수들이 계속 호출되는 이유는 무엇인가요? 게임 오버 후에도 화면을 갱신하는 것이 사용자에게 어떤 정보를 전달하나요?

게임 개발에 있어서 상태 관리와 조건문을 사용한 게임 플로우 제어의 중요성을 이해하는 데 도움을 줍니다. 또한, 게임 오버와 같은 중요한 게임 이벤트를 효과적으로 처리하는 방법에 대한 깊은 이해를 제공합니다.
'''