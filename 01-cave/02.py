import sys  # 프로그램 종료를 위한 라이브러리 가져 오기
import pygame  # pygame 가져 오기
from pygame.locals import QUIT  # 종료 이벤트 타입 가져 오기

pygame.init()  # pygame 모듈 초기화
SURFACE = pygame.display.set_mode((800, 600))  # 화면 표시 영역(가로 800, 세로 600), 튜플 표기에 주의
FPSCLOCK = pygame.time.Clock()  # 지정한 FPS 에 맞춰서 표현이 되도록 도와 준다.


def main():
    while True:  # 게임 루프 - 게임을 종료할 때까지 무한 반복한다.

        for event in pygame.event.get():  # 이벤트 큐 로부터 이벤트를 하나씩 가져 와서 event 변수에 담는다.
            if event.type == QUIT:  # 이벤트 타입이 종료 라면
                pygame.quit()  # pygame 을 종료 시킨다.
                sys.exit()  # 프로그램 도 종료 시킨다.

        SURFACE.fill((0, 255, 0))  # 화면 데이터에 (Red = 0, Green = 255, Blue = 0) 으로 채워 준다.

        pygame.display.update()  # 화면 데이터의 내용을 실제 디스플레이에 반영 한다.

        FPSCLOCK.tick(15)  # 15 FPS 로 동작 하도록 프로그램을 휴식 시킨다.


main()

# Q1. FPSCLOCK.tick() 을 생략해보세요.
# Q2. FPSCLOCK.tick() 의 파라메터를 수정하여 fps 를 변경해 보세요.
# Q3. event 처리 루프를 제거 한다면 어떻게 될까요?
