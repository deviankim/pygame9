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
    score = 0                                               ###
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)                 ###
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
            score += 10                                     ###
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

        SURFACE.fill((0, 255, 0))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render("score is {}".format(score), True, (0, 0, 225))    ###
        SURFACE.blit(score_image, (600, 20))                                            ###

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y - 40))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **점수 시스템의 구현**: `score += 10` 코드는 게임 내에서 어떤 역할을 하며, 점수 시스템이 플레이어의 게임 플레이 경험에 어떤 영향을 미치나요? 점수가 게임의 목표와 도전 의식에 어떻게 기여하는지 설명해 보세요.

2. **화면에 점수 표시하기**: `score_image = sysfont.render("score is {}".format(score), True, (0, 0, 225))`와 `SURFACE.blit(score_image, (600, 20))` 코드는 어떻게 작동하며, 게임 UI에 점수를 표시하는 것이 사용자 경험에 어떤 가치를 추가하나요? 이 방식이 게임의 몰입감과 정보 제공에 어떻게 기여하는지 논의해 보세요.

3. **글꼴 사용과 텍스트 렌더링**: `sysfont = pygame.font.SysFont(None, 36)`를 통해 생성된 폰트 객체의 사용은 게임 개발에서 어떤 의미가 있나요? Pygame에서 텍스트를 렌더링하고 화면에 표시하는 과정이 게임 디자인에서 어떻게 활용될 수 있는지 탐색해 보세요.

4. **게임 오버 메커니즘**: 게임 오버 조건을 검사하고, `game_over` 변수의 상태 변경이 게임 흐름에 어떻게 영향을 미치나요? 게임 오버 상황을 플레이어에게 표시하는 방법(예: `bang_image`를 화면에 표시)이 사용자에게 어떤 감정적 반응을 일으킬 수 있는지 고민해 보세요.

5. 게임을 하드모드를 만들어 봅시다.

6. 우주선 영역만큼 사각형을 그려봅시다. 그리고 무엇을 발견했나요?

7. 우주선 바닥 좌표를 정확하게 계산하려면 어떻게 해야 할까요?

점수 시스템의 설계, UI 요소의 중요성, 텍스트 렌더링 방법, 그리고 게임 오버와 같은 게임 상태 관리의 중요성을 이해하는 데 도움이 됩니다. 또한, 게임의 목표 설정, 사용자 피드백 제공, 그리고 사용자 경험 강화 방법에 대한 통찰력을 제공할 수 있습니다.

'''