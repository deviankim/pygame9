import sys
from random import randint

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    speed = 25  #
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

        #############################################################
        for rock in rocks:
            rock["pos"][2] -= speed
            if rock["pos"][2] < 64:
                rock["pos"] = [randint(-1600, 1600),
                               randint(-1600, 1600), 4095]
        #############################################################

        SURFACE.fill((0, 0, 0))

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

1. **속도의 역할**: `speed` 변수는 게임 내에서 어떤 역할을 합니다? 이 값을 조절함으로써 게임의 난이도나 플레이어의 경험에 어떤 영향을 미치나요?

2. **록의 위치 업데이트**: `rock["pos"][2] -= speed` 구문을 통해 각 록의 z 위치를 감소시키는 것은 어떤 시각적 효과를 만들어내나요? 이러한 방식으로 록의 움직임을 구현하는 것이 왜 중요한가요?

3. **록의 재배치 조건**: 록이 특정 z 위치(`64`) 아래로 내려갔을 때 재배치하는 로직은 어떻게 게임에 다양성을 추가하나요? 록의 새 위치를 랜덤하게 지정하는 것(`randint(-1600, 1600)`)이 게임 플레이에 어떤 영향을 미치며, 이는 플레이어에게 어떤 도전을 제공하나요?

4. **록의 시각적 표현과 인터랙션**: 록이 화면을 가로지르며 점점 작아지는 시각적 효과는 어떻게 구현되나요? `pygame.transform.rotozoom` 함수를 사용하여 록 이미지를 회전시키고 크기를 조정하는 과정이 게임의 몰입감에 어떻게 기여하나요?

객체의 움직임과 재배치 로직, 시각적 효과의 구현, 그리고 게임 오버 조건의 중요성을 이해하는 데 도움을 줍니다. 또한, 게임 디자인에서 플레이어의 행동과 게임 환경 간의 인터랙션을 설계하는 방법에 대한 인사이트를 제공할 수 있습니다.
'''