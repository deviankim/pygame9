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
    bang_image = pygame.image.load("bang.png")  ###

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

        if game_over:                                        ###
            SURFACE.blit(bang_image, (0, ship_y - 40))  ###

        pygame.display.update()

        FPSCLOCK.tick(15)


main()

'''

1. **이미지 로딩과 사용**: `bang_image = pygame.image.load("bang.png")` 구문은 프로그램 내에서 어떤 역할을 하나요? `pygame.image.load` 함수를 사용하여 이미지를 로드할 때, 파일 경로나 이름에 주의해야 하는 이유는 무엇인가요?

2. **게임 오버 시 이미지 표시**: 게임 오버가 되었을 때 `bang_image`를 화면에 표시하는 로직(`SURFACE.blit(bang_image, (0, ship_y - 40))`)은 어떻게 작동하나요? 여기서 `(0, ship_y - 40)`은 어떤 위치를 의미하며, 왜 이 위치에 이미지를 표시하려고 하나요?

3. **조건부 이미지 렌더링**: `if game_over:` 조건문을 사용하여 게임 오버 상태에서만 특정 이미지(`bang_image`)를 표시하는 방식은 사용자 경험에 어떤 영향을 미치나요? 게임 디자인에서 이러한 조건부 렌더링 방식이 갖는 의미와 중요성은 무엇인가요?

4. **게임 오버 피드백의 시각화**: 게임 오버 상황에서 `bang_image`를 사용하는 것이 플레이어에게 어떤 시각적 피드백을 제공하나요? 이러한 시각적 피드백이 게임 플레이어의 이해와 게임의 몰입도에 어떻게 기여할 수 있나요?

pygame 라이브러리를 사용한 이미지 처리, 조건부 로직을 통한 게임 상태 관리, 그리고 게임 오버와 같은 중요한 이벤트에 대한 시각적 피드백 제공 방법을 이해하는 데 도움을 줍니다. 또한, 게임 디자인에서 사용자 경험을 향상시키는 방법에 대한 인사이트를 제공할 수 있습니다.
'''