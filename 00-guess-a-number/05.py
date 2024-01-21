from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("컴퓨터가 생각한 숫자는", computer_number, "입니다")

print("computer_number 는 무엇 일까요?")

player_number = input()
player_number = int(player_number)

print(f"플레이어의 숫자는 {player_number} 입니다.")

if computer_number == player_number:  # if 문을 사용하여 조건을 검사합니다.
    print("축하합니다.")  # 조건이 맞는 경우 (True) 이 블럭을 실행합니다.
    print("당신이 이겼습니다.")  #
else:  # 조건이 맞지 않는 경우 (False) 아래 블럭을 실행합니다.
    print("틀렸습니다.")  #
