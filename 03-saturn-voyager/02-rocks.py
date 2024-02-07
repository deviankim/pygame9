import sys
from random import randint                      #

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    rocks = []                                  #

    rock_image = pygame.image.load("rock.png")  #

    while len(rocks) < 200:                     #
        rocks.append({                          #
            "pos": [randint(-1600, 1600),    #
                    randint(-1600, 1600),    #
                    randint(0, 4095)],    #
            "theta": randint(0, 360)      #
        })                                      #

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        ###################################################################################
        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - 0) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - 0) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))
        ###################################################################################

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()

'''

1. **3D 효과 구현**: 주어진 코드에서는 어떤 방식으로 3D 효과를 시뮬레이션하고 있나요? `rocks` 리스트에 저장된 각각의 객체에 대해 계산된 `xpos`, `ypos`, 그리고 `size`는 화면상의 3D 효과를 어떻게 구현하나요?

2. **록(rock) 객체의 구조와 사용**: 각 `rock` 객체가 가진 `"pos"`와 `"theta"` 속성은 어떤 정보를 나타내며, 이 정보는 어떻게 사용되나요? `"pos"` 배열의 각 요소는 무엇을 의미하며, `"theta"` 값은 어떤 용도로 사용되나요?

3. **록 이미지의 변형과 렌더링**: `pygame.transform.rotozoom` 함수는 어떤 작업을 수행하며, 여기서 사용된 매개변수는 각각 무엇을 의미하나요? `rotated` 이미지가 최종적으로 어떻게 화면에 렌더링되는 과정을 설명해주세요.

4. **수학적 계산의 시각적 표현**: `xpos`, `ypos`, 그리고 `size`를 계산하는 과정에서 사용된 수학적 연산은 어떤 원리에 기반하고 있으며, 이러한 계산이 실제 게임 환경에서 어떤 시각적 결과를 만들어내나요?

5. **록의 배치와 움직임**: 초기에 `rocks` 리스트를 생성하고 채우는 과정에서 랜덤함수를 사용한 의도는 무엇인가요? 이 과정이 게임 환경에 어떤 다양성과 도전을 추가하나요?

3D 효과의 시뮬레이션, 객체 기반 프로그래밍, 이미지 변형 및 렌더링 기술, 그리고 수학적 계산을 시각적 요소에 적용하는 방법을 이해하는 데 도움을 줍니다. 또한, 게임 디자인과 프로그래밍에서 창의적인 접근 방법을 탐색하도록 격려합니다.
'''
