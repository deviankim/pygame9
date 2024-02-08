import sys
from random import randint

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    game_over = False
    score = 0  ########
    speed = 25
    rocks = []
    keymap = []
    ship = [0, 0]
    rock_image = pygame.image.load("rock.png")

    scorefont = pygame.font.SysFont(None, 36)  ########
    sysfont = pygame.font.SysFont(None, 72)
    message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (400, 400)

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

        if not game_over:
            score += 1              ########
            if score % 10 == 0:     ########
                speed += 1          ########

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

        SURFACE.fill((0, 0, 0))
        rocks = sorted(rocks, key=lambda x: x["pos"][2], reverse=True)

        for rock in rocks:
            zpos = rock["pos"][2]
            xpos = ((rock["pos"][0] - ship[0]) << 9) / zpos + 400
            ypos = ((rock["pos"][1] - ship[1]) << 9) / zpos + 400
            size = (50 << 9) / zpos
            rotated = pygame.transform.rotozoom(rock_image, rock["theta"], size / 145)
            SURFACE.blit(rotated, (xpos, ypos))

        if game_over:
            SURFACE.blit(message_over, message_rect)

        score_str = str(score).zfill(6)                                 ###
        score_image = scorefont.render(score_str, True, (0, 255, 0))    ###
        SURFACE.blit(score_image, (700, 50))                            ###

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == '__main__':
    main()


'''

1. **점수 시스템의 구현**: `score` 변수를 사용하여 게임에서 점수를 어떻게 계산하고 있나요? 게임 플레이 중에 점수가 어떻게 증가하며, 이 증가가 게임 경험에 어떤 영향을 미치나요?

2. **점수와 게임 난이도의 관계**: 점수가 일정 수준(`score % 10 == 0`)에 도달할 때마다 `speed`를 증가시키는 로직은 게임의 난이도에 어떤 변화를 주나요? 이러한 방식으로 게임 난이도를 조절하는 것이 플레이어의 동기 부여에 어떻게 작용할 수 있나요?

3. **점수 표시의 시각적 처리**: 점수를 화면에 표시하는 과정에서 `str(score).zfill(6)`과 `scorefont.render` 함수를 사용한 의도는 무엇인가요? `zfill(6)`이 점수 표시에 어떤 시각적 효과를 주며, 이것이 사용자 경험에 어떻게 기여하나요?

4. **점수 표시 위치의 선택**: 점수를 화면의 `(700, 50)` 위치에 표시하는 이유는 무엇인가요? 게임 UI 디자인에서 정보(예: 점수)를 표시하는 위치를 결정할 때 고려해야 할 요소는 무엇인가요?

5. **점수와 게임 오버 메시지의 조화**: 게임 오버가 되었을 때 점수 표시와 "GAME OVER!!" 메시지가 함께 화면에 나타나는 방식은 사용자에게 어떤 메시지를 전달하나요? 게임 오버 시점에서 점수 정보를 제공하는 것이 플레이어에게 어떤 의미가 있을까요?

점수 시스템의 설계, 게임 난이도의 동적 조절, 시각적 정보의 표현 방법, 그리고 사용자 경험(UX) 디자인의 중요성을 이해하는 데 도움을 줍니다. 또한, 게임의 목표 설정과 플레이어의 성취감 증진 방법에 대한 깊은 이해를 제공할 수 있습니다.
'''