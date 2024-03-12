# 변수 선정 - 대소문자 구분/언더바 포함 가능/예약어 사용 불가/마지막 입력값을 저장
# ex) No_1 = 20 (O)// True = 1 (X)
# 변수 작성 시 콤마를 이용하여 연달아 작성도 가능
# a, b = 2, 4

# 입력받기 input
# name = input("이름을 입력하시오 : >>")
# print("당신의 이름은",name+"입니다.")

# 예제 1 - 숫자 하나(2)를 입력받아 구구단을 출력하라

# # 풀이 1)
# num = int(input("숫자를 입력하세요 >>"))
# print(num , "*" , "1","=",(int(num)*1))
# print(num , "*" , "2","=",(int(num)*2))
# print(num , "*" , "3","=",(int(num)*3))

# # 풀이 2)
# print("%d * 1 = %d"%(2,2))
# print("%d * 2 = %d"%(2,4))
# print("%d * 3 = %d"%(2,6))

# # 최종 풀이방법 )
# print('{} * {} = {}'.format(2,1,2*1))
# print('{} * {} = {}'.format(2,2,2*2))
# print('{} * {} = {}'.format(2,3,2*3))       # format 형태 그대로 작성

# num = 3
# print('{} * {} = {}'.format(num,1,num*1))
# print('{} * {} = {}'.format(num,2,num*2))
# print('{} * {} = {}'.format(num,3,num*3))   # 변수를 만들어서 작성

# num =input("원하는 단을 입력하세요 >>")
# num = int(num)                                # 숫자 형태로 바꿔주는 부분(int 타입)
# print('{} * {} = {}'.format(num,1,num*1))
# print('{} * {} = {}'.format(num,2,num*2))
# print('{} * {} = {}'.format(num,3,num*3))