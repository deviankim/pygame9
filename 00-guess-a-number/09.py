from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("컴퓨터가 생각한 숫자는", computer_number, "입니다")

while True:
    print("computer_number 는 무엇 일까요?")
    player_number = input()
    player_number = int(player_number)  # str 타입을 int 타입으로 변환 합니다.
    print("플레이어의 숫자는", player_number, "입니다.")

    print(f"[debug]: type of computer_number is {type(computer_number)}")
    print(f"[debug]: type of player_number is {type(player_number)}")

    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
    else:
        print("틀렸습니다.")
