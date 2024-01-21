from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)

is_in_game = True
score = 100

while is_in_game:
    print("내가 생각한 숫자는 무엇 일까요?")
    player_number = int(input())
    print("입력한 숫자는", player_number, "입니다.")

    if computer_number == player_number:
        print("축하합니다.")
        print("당신이 이겼습니다.")
        is_in_game = False
    elif computer_number < player_number:
        print("그것 보다 작습니다.")
        score = score - 5  
    else:
        print("그것 보다 큽니다.")
        score -= 5  

print(f"점수는 {score} 점 입니다.")  

# Q1. 점수가 50점 이하인 경우에 게임을 종료 하고 "GAME OVER" 를 출력해 보세요.
