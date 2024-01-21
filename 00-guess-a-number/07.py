from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("[", computer_number, "]")

while True:  # while 은 반복문의 가장 기본적인 형태입니다.
    print("내가 생각한 숫자는 무엇 일까요?")
    player_number = int(input())
    print("입력한 숫자는", player_number, "입니다.")

    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
    else:
        print("틀렸습니다.")
