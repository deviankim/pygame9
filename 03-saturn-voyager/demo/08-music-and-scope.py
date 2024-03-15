import sys
from random import randint

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
W = 800
H = 800
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    game_over = False
    score = 0
    speed = 25
    ship_x, ship_y = (0, 0)
    scope_image = pygame.image.load("scope.png")
    rock_image = pygame.image.load("rock.png")

    scorefont = pygame.font.SysFont(None, 36)
    sysfont = pygame.font.SysFont(None, 72)
    message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (400, 400)

    pygame.mixer.music.load("Escape.mp3")
    pygame.mixer.music.play()

    rocks = []
    while len(rocks) < 200:
        rocks.append({
            "pos": [randint(-1600, 1600),
                    randint(-1600, 1600),
                    randint(0, 4000)],
            "theta": randint(0, 360)
        })

    key_set = set([])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key_set.add(event.key)
            elif event.type == KEYUP:
                key_set.remove(event.key)

        if not game_over:
            score += 1
            if score % 10 == 0:
                speed += 1

            if K_LEFT in key_set:
                ship_x -= 30
            if K_RIGHT in key_set:
                ship_x += 30
            if K_UP in key_set:
                ship_y -= 30
            if K_DOWN in key_set:
                ship_y += 30

            for rock in rocks:
                rock["pos"][2] -= speed
                z = rock["pos"][2]
                if z < 64:
                    x = rock["pos"][0]
                    y = rock["pos"][1]

                    if abs(x - ship_x) < 50 and abs(y - ship_y) < 50:
                        game_over = True
                        break

                    rock["pos"] = [
                        randint(-1600, 1600),
                        randint(-1600, 1600),
                        4000,
                    ]

        SURFACE.fill((0, 0, 0))
        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - ship_x) * 500) / zpos + W / 2
            ypos = ((rock["pos"][1] - ship_y) * 500) / zpos + H / 2
            size = (50 * 500) / zpos
            rotated = pygame.transform.rotozoom(rock_image,
                                                rock["theta"],
                                                size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        # SURFACE.blit(scope_image, (0, 0))

        if game_over:
            SURFACE.blit(message_over, message_rect)
            pygame.mixer.music.stop()

        score_str = str(score).zfill(6)
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        SURFACE.blit(score_image, (700, 50))

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()

'''

1. **멀티미디어 통합**: `pygame.mixer.music.load("Escape.mp3")`와 `pygame.mixer.music.play()`를 사용하여 게임에 배경음악을 추가하는 과정은 어떻게 진행되나요? 게임의 몰입감과 사용자 경험에 음악이 어떤 영향을 미치나요?

2. **게임 오버 시 음악 처리**: 게임 오버가 되었을 때 `pygame.mixer.music.stop()` 함수를 호출하는 이유는 무엇인가요? 게임의 다양한 상태(예: 게임 진행 중, 게임 오버)에 따라 오디오 출력을 어떻게 관리해야 하며, 이는 사용자에게 어떤 신호를 제공하나요?

3. **시각적 요소의 추가**: `scope_image`를 화면에 표시하는 과정(`SURFACE.blit(scope_image, (0, 0))`)은 게임의 시각적 구성에 어떤 새로운 요소를 추가하나요? 이러한 시각적 요소가 게임의 테마나 분위기에 어떤 기여를 하며, 게임 디자인에서 시각적 요소의 중요성은 무엇인가요?

4. **키 입력과 캐릭터 움직임**: `KEYDOWN`과 `KEYUP` 이벤트를 사용하여 `keymap` 리스트를 업데이트하고, 이를 기반으로 우주선(또는 캐릭터)의 움직임을 제어하는 방식은 어떤 장점을 가지나요? 동적인 게임 환경에서 사용자 입력을 처리하는 다양한 방법에는 어떤 것들이 있을까요?

5. **동시 키입력 처리**: 키조합 (오른방향키와 아랫방향키 혹은 왼방향키와 아랫방향키)을 허용하려면 코드를 어떻게 수정해야 할까요?


6. **이동 좌표 제한**: 우주선의 (x, y)좌표를 -800 에서 800 사이에만 있도록 제한하려면 어떻게 해야 할까요?  

오디오 및 시각적 요소의 통합, 사용자 입력의 처리, 게임 상태에 따른 적절한 피드백 제공의 중요성을 이해하는 데 도움을 줍니다. 또한, 게임 디자인에서 사용자 경험을 향상시키는 다양한 방법을 탐색하도록 격려합니다.
'''
