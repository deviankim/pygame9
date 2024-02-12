import sys

import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT  ######


class Block:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self):
        pygame.draw.rect(SURFACE, self.color, self.rect)


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))  ######


def main():
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color=color, rect=Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:         #
                if event.key == K_LEFT:         #
                    PADDLE.rect.centerx -= 10   #
                elif event.key == K_RIGHT:      #
                    PADDLE.rect.centerx += 10   #

        SURFACE.fill((0, 0, 0))
        PADDLE.draw()                           #
        for block in BLOCKS:
            block.draw()

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()

'''

1. **패들 객체의 생성과 그리기**: `PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))` 코드를 통해 생성된 패들 객체는 게임에서 어떤 역할을 합니다? `PADDLE.draw()` 메서드 호출이 화면에 패들을 어떻게 표시하나요?

2. **키보드 입력 처리**: `elif event.type == KEYDOWN:` 조건문을 통해 어떻게 사용자의 키보드 입력을 처리하고 있나요? K_LEFT와 K_RIGHT 키 이벤트에 대한 반응으로 패들의 위치는 어떻게 변경되나요?

3. **패들의 움직임 구현**: `PADDLE.rect.centerx -= 10` 및 `PADDLE.rect.centerx += 10` 코드는 패들의 위치를 어떻게 조정하나요? 이러한 방식으로 패들을 좌우로 움직이게 하는 것의 게임 플레이에 어떤 영향을 미치나요?

4. **게임 요소 간의 상호작용**: 패들 객체와 블록 객체들을 같은 `Block` 클래스로부터 생성한 이유는 무엇인가요? 이러한 설계가 게임 개발에서 가져오는 장점은 무엇이며, 게임 내 다른 요소들과의 상호작용을 구현하는 데 어떻게 활용될 수 있나요?

5. **객체 지향 프로그래밍의 활용**: `Block` 클래스를 사용하여 패들과 벽돌을 구현한 것은 객체 지향 프로그래밍의 어떤 원칙을 보여주나요? 이 접근 방식이 게임 코드의 재사용성과 유지 보수에 어떤 이점을 제공하나요?

6. **사용자 인터페이스와 상호작용**: 키보드 입력을 통한 패들의 제어가 사용자 경험에 어떤 영향을 미치나요? 이러한 방식의 입력 처리가 게임의 몰입감과 플레이어의 제어감을 증진시키는 방법에 대해 설명해 보세요.

Pygame 라이브러리를 사용한 입력 처리, 객체 지향 프로그래밍을 통한 게임 요소의 구현, 그리고 사용자 상호작용의 중요성에 대해 이해하는 데 도움을 줍니다.
'''