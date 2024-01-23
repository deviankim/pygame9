from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작합니다.")

computer_number = randint(1, 5)
print("[", computer_number, "]")

is_in_game = True  # 게임이 진행중인지 확인 하도록 상태 변수를 선언 합니다.

while is_in_game:  # while 의 조건을 변수로 변경 하여 변수에 따라 게임이 종료 되게 합니다.
    print("내가 생각한 숫자는 무엇 일까요?")
    player_number = int(input())
    print("입력한 숫자는", player_number, "입니다.")

    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
        is_in_game = False  # 게임이 종료될 수 있게 변수값을 바꿉니다.
    else:
        print("틀렸습니다.")

# Q1. is_in_game 변수를 사용하지 없어도 while 문을 벗어날 수 있을까요?
