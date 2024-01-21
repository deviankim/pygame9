from random import randint              # random 에서 randint 함수를 가져옵니다.

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작합니다.")

computer_number = randint(1, 5)   # [1,2,3,4,5] 중의 하나를 랜덤 선택 하여 computer_number 변수에 할당 합니다.
print("[", computer_number, "]")        # computer_number 가 무엇인지 print() 로 확인

# Q1. 맨 위의 from random import randint 를 지워볼까요? 어떻게 되는지 봅시다.
