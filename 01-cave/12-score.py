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
    score = 0  ###
    slope = randint(1, 6)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")

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

        if not game_over:
            score += 10  # 점수 누적
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)

            edge.move_ip(10, slope)
            holes.append(edge)

            del holes[0]
            holes = [x.move(-10, 0) for x in holes]

            if holes[0].top > ship_y or \
                    holes[0].bottom < ship_y + 80:
                game_over = True

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))
        print('score', score)  ###

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y - 40))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **점수 시스템의 구현**: `score += 10` 구문은 어떤 상황에서 실행되며, 이 코드가 게임 내에서 어떤 역할을 합니다? 게임의 어떤 행동이나 이벤트가 점수 증가와 연결되어 있나요?

2. **점수의 의미와 사용자 피드백**: `print('score', score)`를 통해 콘솔에 점수를 출력하는 방식은 개발 과정에서 어떤 이점을 제공하나요? 실제 게임에서 사용자에게 점수를 어떻게 표시하는 것이 좋을까요?

3. **게임 오버와 점수 관계**: 게임이 오버되었을 때 점수 계산이 중지되는 방식은 사용자에게 어떤 메시지를 전달하나요? 게임 오버가 되었을 때 사용자의 최종 점수를 표시하는 것이 게임 경험에 어떻게 기여할 수 있나요?

4. **점수 계산 로직의 의미**: 이 게임에서 점수를 시간이나 거리에 기반하여 계산하는 방식은 게임 플레이어에게 어떤 동기를 부여하나요? 점수를 통해 플레이어의 성취감을 어떻게 증진시킬 수 있을까요?

점수 시스템의 중요성, 사용자 피드백의 역할, 그리고 게임 디자인에서의 동기 부여 기법을 이해하는 데 도움을 줍니다. 또한, 플레이어에게 명확한 목표와 성취감을 제공하는 방법에 대해 생각해 볼 수 있게 합니다.
'''