# randint() 함수가 정의 되어 있지 않아 오류가 났습니다.
# random 라이브러리를 통해 미리 정의된 randint() 함수를 불러 와야 합니다.
# 방법은 두 가지 중 하나를 이용 하면 됩니다.
# 1. `from random import randint` 를 직접 타이핑 합니다.
# 2. 빨간 밑줄이 그어진 곳으로 커서를 이동한 후, alt+enter 키를 눌러서 "import 'random.randint'" 선택
from random import randint

print("안녕하세요 플레이어 ??? 님")
print("숫자 맞추기 게임을 시작 합니다.")

computer_number = randint(1, 5)
print("컴퓨터가 생각한 숫자는", computer_number, "입니다")

