import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE  ###

pygame.init()
pygame.key.set_repeat(5, 5)         ###
SURFACE = pygame.display.set_mode((800, 600))

FPSCLOCK = pygame.time.Clock()


def main():
    ship_y = 250                                                    ###
    velocity = 0
    ship_image = pygame.image.load("ship.png")

    while True:
        is_space_down = False                                       ###

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:    ###
                is_space_down = True

        velocity += -3 if is_space_down else 3                      ###
        ship_y += velocity

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **키보드 이벤트 처리**: `from pygame.locals import QUIT, KEYDOWN, K_SPACE` 구문에서 `KEYDOWN`과 `K_SPACE`는 프로그램 내에서 어떤 역할을 합니다? 이 코드를 통해 어떤 사용자 입력을 처리할 수 있나요?

2. **키 반복 설정**: `pygame.key.set_repeat(5, 5)` 호출의 목적은 무엇인가요? 이 설정이 게임 내에서 어떤 사용자 경험을 제공하며, `set_repeat` 함수의 매개변수 `(5, 5)`는 어떤 의미를 가지나요?

3. **조건에 따른 속도 변경**: `velocity += -3 if is_space_down else 3` 구문은 어떻게 작동하나요? 이 코드가 게임 내의 객체 움직임에 어떤 영향을 미치며, `is_space_down` 변수의 상태는 어떻게 결정되나요?

4. **스페이스바 입력과 게임 물리**: 스페이스바가 눌렸을 때 (`is_space_down = True` 상태)와 눌리지 않았을 때 (`is_space_down = False` 상태)의 `velocity` 값 변화는 게임의 어떤 물리적 행동을 시뮬레이션하나요? 이러한 입력 처리 방식이 게임 플레이에 어떤 다이내믹을 추가하나요?

'''
# Q1. pygame.key.set_repeat 를 주석처리해보세요. 어떻게 되나요?
# Q2. FPSCLOCK.tick() 의 파라메터를 수정하여 fps 를 변경해 보세요.
