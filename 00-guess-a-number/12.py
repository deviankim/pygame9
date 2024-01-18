from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print(f"[debug]: computer_number is {computer_number}")

is_in_game = True
score = 100  # 점수를 담을 변수 score 를 선언합니다.

while is_in_game:
    print("computer_number 는 무엇 일까요?")
    player_number = input()
    player_number = int(player_number)
    print(f"플레이어의 숫자는 {player_number} 입니다.")

    print(f"[debug]: type of computer_number is {type(computer_number)}")
    print(f"[debug]: type of player_number is {type(player_number)}")

    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
        is_in_game = False
    elif computer_number < player_number:
        print("그것 보다 작습니다.")
        score = score - 5  # 틀렸을 경우 5점을 깎습니다.
    else:
        print("그것 보다 큽니다.")
        score -= 5  # -= 로 간소하게 표현할 수 있습니다.

print(f"점수는 {score} 점 입니다.")  # 마지막으로 점수를 표시하고 프로그램이 끝납니다.
