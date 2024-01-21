from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("컴퓨터가 생각한 숫자는", computer_number, "입니다")

print("내가 생각한 숫자는 무엇 일까요?")
player_number = input()
print("플레이어의 숫자는", player_number, "입니다.")

while True:  # while 뒤의 조건이 만족할 동안 아래 블럭을 반복 합니다.
    # 키보드로 아래 블럭을 선택한 다음, 탭(Tab)을 한번 눌러서 들여쓰기를 넣어 줍니다.
    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
    else:
        print("틀렸습니다.")
