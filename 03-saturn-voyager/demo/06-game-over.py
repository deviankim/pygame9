import sys
from random import randint

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    game_over = False  #######################
    speed = 25
    rocks = []
    keymap = []
    ship = [0, 0]
    rock_image = pygame.image.load("rock.png")

    ###  새 코드 시작
    sysfont = pygame.font.SysFont(None, 72)
    message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (400, 400)
    ###  새 코드 종료

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
            elif event.type == KEYDOWN:
                if not event.key in keymap:
                    keymap.append(event.key)
            elif event.type == KEYUP:
                keymap.remove(event.key)

        if not game_over:   #########
            # 들여쓰기 시작
            if K_LEFT in keymap:
                ship[0] -= 30
            elif K_RIGHT in keymap:
                ship[0] += 30
            elif K_UP in keymap:
                ship[1] -= 30
            elif K_DOWN in keymap:
                ship[1] += 30

            for rock in rocks:
                rock["pos"][2] -= speed
                if rock["pos"][2] < 64:
                    if abs(rock["pos"][0] - ship[0]) < 50 and \
                            abs(rock["pos"][1] - ship[1]) < 50:
                        game_over = True
                    rock["pos"] = [randint(-1600, 1600),
                                   randint(-1600, 1600), 4095]
            # 들여쓰기 종료

        SURFACE.fill((0, 0, 0))
        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - ship[0]) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - ship[1]) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        if game_over:                                   ###
            SURFACE.blit(message_over, message_rect)    ###

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()


'''
이 코드에서 새로 추가된 게임 오버 화면과 관련된 부분을 기반으로 만들 수 있는 교육용 질문은 다음과 같습니다:

1. **게임 오버 메시지의 시각적 표현**: 게임 오버 시 화면에 "GAME OVER!!" 메시지를 표시하는 과정에서 사용된 `pygame.font.SysFont`와 `render` 함수는 어떤 역할을 합니다? 이 코드가 게임의 사용자 경험에 어떤 영향을 미치나요?

2. **메시지 위치의 중앙 정렬**: `message_rect.center = (400, 400)` 구문은 메시지를 화면의 어느 위치에 표시하도록 설정하나요? 이 위치가 사용자에게 메시지를 효과적으로 전달하는 이유는 무엇인가요?

3. **조건부 메시지 렌더링**: `if game_over:` 조건문을 통해 게임 오버 상태에서만 특정 메시지를 표시하는 방식은 게임 플로우에 어떻게 기여하나요? 이러한 조건부 렌더링이 게임 디자인에서 왜 중요한가요?

4. **게임 상태 관리와 사용자 피드백**: 게임 오버 상태를 관리하고 사용자에게 직접적인 피드백을 제공하는 이 코드의 구현이 게임 플레이의 명확성과 사용자의 이해도에 어떻게 기여하나요? 게임 오버와 같은 중요한 이벤트에 대한 명확한 피드백이 사용자의 게임 경험에 왜 중요한가요?

사용자 인터페이스(UI) 디자인, 게임 상태 관리, 조건부 렌더링의 적용, 그리고 텍스트 사용을 이해하는 데 도움을 줍니다. 또한, 게임 디자인에서 사용자에게 명확하고 직관적인 피드백을 제공하는 방법에 대한 인사이트를 제공할 수 있습니다.
'''