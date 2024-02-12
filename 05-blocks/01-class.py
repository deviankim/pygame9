import sys

import pygame
from pygame.locals import QUIT, Rect


class Block:                                            #
    def __init__(self, color, rect):                    #
        self.color = color                              #
        self.rect = rect                                #

    def draw(self):                                     #
        pygame.draw.rect(SURFACE, self.color, self.rect)  #


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    block = Block(color=(255, 0, 0), rect=Rect(100, 50, 80, 30))    ###
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))
        block.draw()                                                ###

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()

'''

1. **클래스 생성과 초기화**: `Block` 클래스의 `__init__` 메서드는 어떤 파라미터를 받으며, 이들은 클래스 내에서 어떤 역할을 수행하나요? 객체 초기화 시에 이 파라미터들이 어떻게 사용되는지 설명해주세요.

2. **객체의 메서드 사용**: `Block` 클래스에 정의된 `draw` 메서드는 어떤 기능을 하나요? 이 메서드가 호출될 때, Pygame 라이브러리의 어떤 함수를 사용하여 무엇을 그리나요?

3. **객체 지향 프로그래밍의 실제 적용**: `Block` 클래스를 사용하여 생성된 `block` 객체의 `draw` 메서드 호출 과정은 객체 지향 프로그래밍(OOP) 원칙 중 어떤 것을 잘 보여주나요? 이러한 방식이 게임 개발에 어떤 장점을 가지나요?

4. **속성의 활용**: `Block` 클래스의 인스턴스 변수인 `color`와 `rect`는 각각 어떤 데이터를 저장하며, 이 데이터는 게임 내에서 어떻게 활용되나요? `color`와 `rect` 파라미터를 통해 다양한 블록을 어떻게 커스터마이징할 수 있나요?

5. **그래픽 요소의 구현**: Pygame에서 `pygame.draw.rect` 함수를 사용하는 방법을 통해, 게임 개발자는 어떻게 쉽게 그래픽 요소를 화면에 추가할 수 있나요? `Block` 클래스의 `draw` 메서드 내에서 이 함수를 사용하는 것이 왜 유용한가요?

6. **클래스의 재사용성**: `Block` 클래스를 어떻게 다양한 색상, 크기, 위치의 블록을 생성하는 데 재사용할 수 있나요? 이 클래스를 활용하여 게임 내 다른 유사한 요소들을 어떻게 관리할 수 있나요?

클래스의 정의와 객체의 생성, 초기화, 메서드 사용 방법을 이해하고, Pygame 라이브러리를 사용한 게임 개발에서 객체 지향 프로그래밍의 중요성과 그래픽 요소 구현 방법을 학습하는 데 도움이 됩니다.
'''