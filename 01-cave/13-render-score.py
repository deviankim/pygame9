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
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)  ###
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
            score += 10
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
        score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))    ###
        SURFACE.blit(score_image, (600, 20))                        ###

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y - 40))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **폰트 설정과 사용**: `sysfont = pygame.font.SysFont(None, 36)` 구문은 프로그램 내에서 어떤 역할을 합니다? `None`과 `36`은 각각 어떤 의미를 가지며, 이 폰트 설정은 게임 내의 텍스트 표시에 어떻게 사용되나요?

2. **점수 표시 로직**: `score_image = sysfont.render("score is {}".format(score), True, (0, 0, 225))` 구문은 어떤 작업을 수행하나요? 이 코드에서 `True`와 `(0, 0, 225)`는 각각 어떤 파라미터를 의미하며, `score` 변수의 값을 문자열로 어떻게 표현하고 있나요?

3. **점수 위치 설정**: `SURFACE.blit(score_image, (600, 20))`에서 `(600, 20)`은 점수가 화면에 표시되는 위치를 결정합니다. 이 좌표값은 화면의 어느 부분을 가리키며, 점수를 이 위치에 표시하는 것이 사용자 경험 측면에서 어떤 이점이 있나요?

4. **게임 UI 디자인**: 게임 화면에 점수를 표시하는 것이 게임 플레이어에게 어떤 영향을 미칠 수 있나요? 게임 내에서 점수와 같은 정보를 시각적으로 표현하는 것이 중요한 이유는 무엇인가요?

폰트 설정 및 텍스트 렌더링 방법, 게임 내 정보 표시의 중요성, 그리고 사용자 인터페이스(UI) 디자인의 기본 원리를 이해하는 데 도움을 줍니다. 또한, 게임 플레이어에게 명확하고 유익한 피드백을 제공하는 방법에 대한 인사이트를 제공할 수 있습니다.
'''