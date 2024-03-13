import sys
from random import randint

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN  ###

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    speed = 25
    rocks = []
    keymap = []     #########
    ship = [0, 0]   #########
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
            elif event.type == KEYDOWN:         #
                if not event.key in keymap:     #
                    keymap.append(event.key)    #
            elif event.type == KEYUP:           #
                keymap.remove(event.key)        #

        if K_LEFT in keymap:                    #
            ship[0] -= 30                       #
        elif K_RIGHT in keymap:                 #
            ship[0] += 30                       #
        elif K_UP in keymap:                    #
            ship[1] -= 30                       #
        elif K_DOWN in keymap:                  #
            ship[1] += 30                       #

        for rock in rocks:
            rock["pos"][2] -= speed
            if rock["pos"][2] < 64:
                rock["pos"] = [randint(-1600, 1600),
                               randint(-1600, 1600), 4095]

        SURFACE.fill((0, 0, 0))
        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - ship[0]) << 9) / zpos + 400   ############
            ypos = ((rock["pos"][1] - ship[1]) << 9) / zpos + 400   ############
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()


'''

1. **키 입력의 추적과 관리**: `keymap` 리스트는 어떤 목적으로 사용되며, 이를 통해 어떤 문제를 해결하고 있나요? `KEYDOWN`과 `KEYUP` 이벤트를 사용하여 `keymap` 리스트를 업데이트하는 방식은 사용자 입력을 어떻게 더 정확하게 처리하나요?

2. **동시 키 입력의 처리**: 여러 키를 동시에 누르는 경우(예: 왼쪽과 위쪽 화살표), 이 코드는 어떻게 반응하나요? 이러한 입력 방식이 게임 플레이에 어떤 유연성을 제공하며, 이는 사용자 경험에 어떤 영향을 미치나요?

3. **우주선의 위치 조정**: `ship` 배열을 사용하여 우주선의 위치를 조정하는 로직(`ship[0] -= 30`, `ship[1] -= 30` 등)은 게임 내에서 어떤 효과를 만들어내나요? 이 방식으로 우주선의 움직임을 구현하는 것이 게임의 몰입감과 조작감에 어떻게 기여할 수 있나요?

4. **우주선 위치에 따른 록의 렌더링**: `xpos`와 `ypos`를 계산할 때 `ship[0]`과 `ship[1]`을 사용하는 이유는 무엇인가요? 이 로직이 화면에 표시되는 록의 위치에 어떤 영향을 미치며, 이는 게임 내에서 어떤 시각적 효과를 생성하나요?

5. **게임의 인터랙티브 요소 개선**: 이러한 키 입력과 우주선 이동 로직을 통해 게임에 어떤 인터랙티브 요소가 추가되었나요? 플레이어가 직접 우주선을 조종할 수 있게 함으로써 게임의 재미와 도전 요소는 어떻게 변화하나요?

키 입력 처리, 동적 객체 이동, 그리고 게임 개발에서의 인터랙티브 디자인의 중요성을 이해하는 데 도움을 줍니다. 또한, 게임 프로그래밍에서 사용자 입력에 기반한 동적인 게임 환경을 구성하는 방법에 대한 깊은 이해를 제공할 수 있습니다.
'''