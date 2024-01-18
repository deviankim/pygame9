from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print(f"[debug]: computer_number is {computer_number}")

print("computer_number 는 무엇 일까요?")
player_number = input()
print(f"플레이어의 숫자는 {player_number} 입니다.")
