import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    ship_image = pygame.image.load("ship.png")  ###

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 255, 0))

        SURFACE.blit(ship_image, (0, 0))  ###

        pygame.display.update()

        FPSCLOCK.tick(15)


main()

'''

1. **이미지 로딩**: `ship_image = pygame.image.load("ship.png")` 구문은 프로그램에서 어떤 역할을 하나요? `pygame.image.load` 함수는 어떤 종류의 파일을 처리할 수 있으며, 이 함수를 사용할 때 주의해야 할 점은 무엇인가요?

2. **이미지 표시**: `SURFACE.blit(ship_image, (0, 0))` 구문이 실행되면 화면에 어떤 변화가 일어나나요? `blit` 메소드의 두 번째 매개변수 `(0, 0)`은 무엇을 의미하며, 이 값을 변경하면 이미지는 어떻게 표시되나요?

3. **게임 화면 갱신**: 이미지를 화면에 추가한 후 `pygame.display.update()` 함수를 호출하는 이유는 무엇인가요? 이 함수 호출 없이도 이미지가 화면에 표시되나요?

'''