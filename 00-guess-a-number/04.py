from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작합니다.")

computer_number = randint(1, 5)
print("[", computer_number, "]")

print("내가 생각한 숫자는 무엇 일까요?")
player_number = int(input())
print("입력한 숫자는", player_number, "입니다.")

if computer_number == player_number:  # if 문을 사용하여 조건을 검사합니다.
    print("축하합니다.")  # 조건이 맞는 경우 (True) 이 블럭을 실행합니다.
    print("당신이 이겼습니다.")  #

# Q1. int() 과정을 생략 하면 어떻게 될까요?
# Q2. 왜 비교 연산자는 (==) 일까요? equal(=) 을 하나만 쓰면 편해서 좋지 않을까요?
