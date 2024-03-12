# 랜덤으로 섞어서 출력하시오
# [[1,2,3,4,5],[6,7,8,9,10],,,,,,[21,22,23,24,25]]
# 모든 수를 랜덤하게 섞은 후 리스트에 넣어라.

import random

num = random.randint(1,100)
# print(num)

# 숫자맞추기 프로그램 재현
# 1 - 10까지의 숫자를 랜덤으로 생성 후 생성숫자를 맞추는 프로그램입니다. 
a = []
while True :
    in_num = int(input("선택한 숫자를 입력하시오 >>"))
    if num > in_num :
        print('입력한 숫자보다 큽니다.')
    elif num < in_num :
        print("입력한 숫자보다 작습니다.")
    else :
        print('정답입니다.')
        break
    a.append(in_num)
print('입력하신 숫자는 {} 이며 총 도전횟수는 {}회입니다.'.format(a,len(a)))    