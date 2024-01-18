from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print(f"[debug]: computer_number is {computer_number}")

is_in_game = True

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
    else:
        print("틀렸습니다.")
