# a = 1 # a는 변수
# print(a) # 이름 뒤에 ()이 있으면 함수 
# C1 # 대문자 or 뒤에 괄호가 없으면 클래스


# 함수 정의 -> def 이름()
import co

coffee = 0


while True :
    print("-" * 50)
    print("1. 보통커피")
    print("2. 설탕커피")
    print("3. 블랙커피")
    coffee = int(input("어떤 커피를 주문하시겠어요? >>"))
    print()
    # 함수 사용방법 -> 함수호출 : 함수명(변수명)
    co.machine(coffee)

