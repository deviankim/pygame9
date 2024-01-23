from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작합니다.")

computer_number = randint(1, 5)
print("[", computer_number, "]")

is_in_game = True
score = 100                             # 점수를 담을 변수 score 를 선언 합니다.

while is_in_game:
    print("내가 생각한 숫자는 무엇 일까요?")
    player_number = int(input())
    print("입력한 숫자는", player_number, "입니다.")

    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
        is_in_game = False
    elif computer_number < player_number:
        print("그것 보다 작습니다.")
        score = score - 5               # 틀렸을 경우 5점을 깎습니다.
    else:
        print("그것 보다 큽니다.")
        score = score - 5               # -= 로 간단하게 표현할 수 있습니다.

print(f"점수는 {score} 점 입니다.")        # 마지막으로 점수를 표시하고 프로그램이 끝납니다.

# Q1. score = score - 5 를 간단하게 변경해 봅시다.
