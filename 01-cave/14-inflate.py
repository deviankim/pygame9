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
    sysfont = pygame.font.SysFont(None, 36)
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
                edge.inflate_ip(0, -20)  ###

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
                                     True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20))

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y - 40))

        pygame.display.update()

        FPSCLOCK.tick(15)


main()


'''

1. **Rect 객체의 변형**: `edge.inflate_ip(0, -20)` 구문은 `edge` 객체에 어떤 변화를 주나요? 여기서 사용된 `inflate_ip` 메소드는 `Rect` 객체의 크기를 어떻게 조정하며, 인자 `(0, -20)`은 구체적으로 무엇을 의미하나요?

2. **장애물 크기 조정의 영향**: 장애물의 크기를 조정하는 이 코드가 게임 플레이에 어떤 영향을 미칠 수 있나요? 장애물의 높이를 줄이는 것이 게임의 난이도나 플레이어의 전략에 어떻게 영향을 줄 수 있나요?

3. **동적 게임 환경 설계**: 장애물의 크기를 런타임에 조정하는 이유는 무엇인가요? 게임 디자인에서 동적으로 변화하는 환경을 구현하는 것이 플레이어의 경험에 어떻게 기여할 수 있나요?

4. **게임 난이도 조절 메커니즘**: `slope`의 조건에 따라 장애물의 크기를 조정하는 로직이 게임의 난이도 조절에 어떻게 활용될 수 있나요? 게임의 진행 상황에 따라 난이도를 조절하는 다양한 방법에는 어떤 것들이 있을까요?

5. 게임을 하드모드를 만들어 봅시다.

6. 우주선 영역만큼 사각형을 그려봅시다. 그리고 무엇을 발견했나요?

7. 우주선 바닥 좌표를 정확하게 계산하려면 어떻게 해야 할까요?

`Rect` 객체와 같은 기본적인 도형을 활용하여 게임 내 요소의 동적 변화를 구현하는 방법, 그리고 게임 난이도와 플레이어 경험 사이의 관계를 이해하는 데 도움을 줍니다. 또한, 게임 디자인에서 동적 환경과 난이도 조절의 중요성을 강조합니다.

'''