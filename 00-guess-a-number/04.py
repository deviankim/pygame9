from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("컴퓨터가 생각한 숫자는", computer_number, "입니다")

print("computer_number 는 무엇 일까요?")  # 숫자를 맞춰 보라고 안내
player_number = input()  # input() 함수로 키보드 입력을 받을 수 있다.
print("플레이어의 숫자는", player_number, "입니다.")  # 플레이어가 입력한 숫자를 보여줍니다.
