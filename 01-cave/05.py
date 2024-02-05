import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE  # KEYDOWN, K_SPACE 상수 가져오기

pygame.init()
pygame.key.set_repeat(5, 5)  # 키 이벤트를 지속적으로 발생시킨다.
SURFACE = pygame.display.set_mode((800, 600))

FPSCLOCK = pygame.time.Clock()


def main():
    ship_y = 250  # 우주선의 y 좌표를 250 에서 시작 하도록 초기값 할당
    velocity = 0
    ship_image = pygame.image.load("ship.png")

    while True:
        is_space_down = False  # space 가 눌러졌는지 확인하는 상태 변수

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:  # 스페이스가 눌러졌는지 조건 검사
                is_space_down = True

        velocity += -3 if is_space_down else 3  # 스페이스가 눌러지면 위로 힘을 주고, 아니면 아래로 힘이 가게 한다.
        ship_y += velocity

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, ship_y))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()

# Q1. pygame.key.set_repeat 를 주석처리해보세요. 어떻게 되나요?
# Q2. FPSCLOCK.tick() 의 파라메터를 수정하여 fps 를 변경해 보세요.
