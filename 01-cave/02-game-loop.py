import sys                                      ######
import pygame                                   ######
from pygame.locals import QUIT                  ######

pygame.init()                                   ######
SURFACE = pygame.display.set_mode((800, 600))   ######
FPSCLOCK = pygame.time.Clock()                  ######


def main():
    # 삭제 print("main 함수가 실행 됩니다.")
    while True:                                 ######

        '''InputEvent'''
        for event in pygame.event.get():        ######
            if event.type == QUIT:              ######
                pygame.quit()                   ######
                sys.exit()                      ######

        '''Update'''

        '''Rendering'''
        SURFACE.fill((0, 255, 0))               ######

        pygame.display.update()                 ######

        FPSCLOCK.tick(15)                       ######


main()

'''

1. **라이브러리 임포트**: `import sys`와 `import pygame` 구문은 프로그램에서 어떤 역할을 하나요? `from pygame.locals import QUIT`는 무엇을 의미하며, 왜 이 구문이 필요한가요?

2. **pygame 초기화**: `pygame.init()` 함수는 pygame 프로그램을 시작하기 전에 왜 필요한가요? 이 함수 없이 pygame 프로그램을 실행할 수 있나요?

3. **게임 화면 설정**: `SURFACE = pygame.display.set_mode((800, 600))` 코드는 프로그램에서 어떤 역할을 합니다? `(800, 600)`은 어떤 의미를 가지나요?

4. **게임 루프**: `while True:` 구문은 프로그램에서 어떤 기능을 수행하나요? 이 무한 루프는 게임 개발에서 왜 중요한가요?

5. **이벤트 처리**: `for event in pygame.event.get():` 구문은 어떤 작업을 수행하나요? `if event.type == QUIT:` 구문이 실행되면 어떤 일이 발생하나요?

6. **화면 갱신**: `pygame.display.update()` 함수의 역할은 무엇인가요? 이 함수는 왜 필요하며, 어떤 일을 수행하나요?

7. **프레임 속도 제어**: `FPSCLOCK.tick(15)` 코드는 프로그램에서 어떤 기능을 합니다? `15`는 무엇을 의미하며, 이 값을 변경하면 어떤 영향을 미치나요?

'''