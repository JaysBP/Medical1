# random 함수
from random import *
# print(random()) 
# print(int(random()*10)) # 0.0 ~ 1.0 미만의 임의의 값이 생성

# print(int(random()*10+1)) # 0.0 ~ 1.0 이하의 임의의 값이 생성

# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1,46))   # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1,45))# 1 ~ 45 이하의 임의의 값 생성

# 예제 1) 1 ~ 10 사이의 숫자를 입력받아 랜덤한 숫자와 비교해
# 같으면 당첨// 다르면 [] 일치하지 않습니다.

# ch = int(input("1부터 10까지의 정수 중 하나를 고르시오 >>  "))
# num = int(randint(1,10))
# if ch == num :
#     print(" 경 당첨 축!!")
# else :
#     print(" 랜덤숫자는 {}로 일치하지 않습니다.".format(ch))