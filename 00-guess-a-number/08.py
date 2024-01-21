from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("[", computer_number, "]")

is_in_game = True

while is_in_game:
    print("내가 생각한 숫자는 무엇 일까요?")
    player_number = int(input())
    print("입력한 숫자는", player_number, "입니다.")

    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
        is_in_game = False
    elif computer_number < player_number:  # elif 를 써서 컴퓨터 숫자가 더 작을 경우를 안내 합니다.
        print("그것 보다 작습니다.")            #
    elif player_number < computer_number:
        print("그것 보다 큽니다.")              #

# Q1. 마지막 elif 를 더 간단하게 변경해볼까요?
