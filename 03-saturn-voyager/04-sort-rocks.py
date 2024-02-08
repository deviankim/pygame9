import sys
from random import randint

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    speed = 25
    rocks = []

    rock_image = pygame.image.load("rock.png")

    while len(rocks) < 200:
        rocks.append({
            "pos": [randint(-1600, 1600),
                    randint(-1600, 1600),
                    randint(0, 4095)],
            "theta": randint(0, 360)
        })

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for rock in rocks:
            rock["pos"][2] -= speed
            if rock["pos"][2] < 64:
                rock["pos"] = [randint(-1600, 1600),
                               randint(-1600, 1600), 4095]

        SURFACE.fill((0, 0, 0))
        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)  ###

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - 0) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - 0) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()


'''

1. **목록 정렬의 목적**: `rocks` 리스트를 `z` 위치에 따라 정렬하는 이유는 무엇인가요? 이 정렬 과정이 시각적 표현에 어떤 영향을 미치며, 왜 `reverse=True` 옵션을 사용했나요?

2. **람다 함수의 사용**: `key=lambda x: x["pos"][2]`에서 람다 함수를 사용하는 이유는 무엇인가요? 람다 함수가 이 컨텍스트에서 어떻게 작동하며, 이를 통해 어떤 값에 기반한 정렬을 수행하나요?

3. **3D 효과 및 깊이감 구현**: 정렬된 `rocks` 리스트를 화면에 렌더링함으로써 어떤 시각적 효과나 깊이감을 구현할 수 있나요? 가까이 있는 객체부터 먼저 렌더링하는 것이 사용자에게 어떤 시각적 정보를 제공하나요?

4. **게임 성능과 정렬 로직**: 매 프레임마다 `rocks` 리스트를 정렬하는 것이 게임 성능에 어떤 영향을 미칠 수 있나요? 큰 데이터 세트를 다룰 때 이러한 정렬 로직의 성능을 어떻게 최적화할 수 있을까요?

정렬 알고리즘의 중요성, 람다 함수와 같은 고급 기능의 사용 방법, 그리고 3D 효과 및 깊이감을 시각적으로 구현하는 기법을 이해하는 데 도움을 줍니다. 또한, 게임 성능 최적화와 관련된 고려 사항에 대해 생각하게 합니다.
'''