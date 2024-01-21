from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("컴퓨터가 생각한 숫자는", computer_number, "입니다")

print("내가 생각한 숫자는 무엇 일까요?")               #
player_number = int(input())                    # input() 함수로 키보드 입력을 받고, int() 로 숫자 타입으로 변경한다.
print("플레이어의 숫자는", player_number, "입니다.")  # 플레이어가 입력한 숫자를 보여줍니다.
