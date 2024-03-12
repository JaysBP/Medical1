# # Day 4 복습

#  변수 선택 -> bool, int, float, str

#  형태 - list, tuple, dict -> [] , {}, () 로 구분되어질 수 있다. 
#  정수형 - %d // 실수형 - %f // 문자열 - %s 의 형태로 작성가능.

# input : 입력 <-> print : 출력
# input(본래 콘솔 창에서 입력을 받는 것-> 안에 무언가를 작성하면 콘솔 창에 띄워서 입력할 수 있게 함.)
# 변수를 받고 입력하면 변수에 그 입력한 값이 저장되는 형태
# print(작성한 값 자체를 콘솔창에 나타내는 것.)

# ex) n1 = input("첫번째 수를 입력하세요 >>") // n2 = input("두번째 수를 입력하세요 >>")
# n1 * n2 값을 출력하세요 -> n1  = 10, n2 = 3
# n1 = int(input("첫번째 수를 입력하세요 >>"))
# n2 = int(input("두번째 수를 입력하세요 >>"))

# print("{} * {} = {}".format(n1,n2,n1*n2))


#  조건문 - if/elif/else -> 조건문 상 if만 작성할 수 있음. (elif or else 생략가능)
#  최초 if에서부터 시작되어 해당 조건이 거짓일 때 차후 elif or else로 넘어가서 실행
#  만약 실행문을 비우거나 생략하기 위해선 pass 활용 -> if a = 3 : // pass
# a = 3
# if a == 0 :
#     print("if문 실행")                  # 실행문에 있는 모든 부분이 한번에 실행됨.
# elif a == 1 :
#     print('첫번째 elif문 실행')
# elif a == 2 :
#     print('두번째 elif문 실행')
# elif a == 3 :
#     print('세번째 elif문 실행')
# else :
#     print("else문 실행")

#  중첩 if문 - 0보다 크면 양수, 작으면 음수를 출력 // 10보다 작으면 [10보다 작음], 크면 [큼]출력
# n = 8
# if n >= 0 :
#     print('양수')
#     if n > 10 :
#         print('[10보다 크다.]')
#     else :
#         print("[10보다 작다.]")
# else :
#     print("음수")
    
# if n >= 0 and n <= 10 :
#     print('양수')
#     print("10보다 작음")
# elif n >= 0 and n > 10 :
#     print("양수")
#     print('10보다 크다')
# else :
#     print('음수')
    
# 예제 1) 숫자 하나를 입력받아 짝수면 짝수, 홀수면 홀수
# n = int(input("원하는 수를 입력하시오 >>"))
# if n % 2 == 0 :
#     print("[짝수]")
# else :
#     print("[홀수]")

# 예제 2) 90점 이상 A, 90점 이하는 F출력
# score = 95
# if score >= 90 :
#     if score >= 98 :
#         print("A+")
#     elif score >= 90 and score <= 93 :
#         print("A-") 
#     elif score > 93 and score < 98 :
#         print("A")
# else :
#     print("F")
    
    
# list - 변수명 선언 후 요소를 [] 내에 채워주는 것, 각자의 요소가 변수로 판단(수,문자,리스트 모두 가능)
list = ['홍길동', 100]
list1 = [[2,4,6],[1,3,5]]
list2 = [True, False, True]
list3 = [True, 30, 42.195, [6,8,9,11],'Hello']

# 인덱싱- 리스트 검색 및 접근 // index는 0부터 시작
# print(list[0])
# print(list1[1][1])
# print(list2[1])
# print(list3[-1])
# print(list1[1][0])
# print(list1[1][2])

# 인덱싱을 통해 리스트 내 특정 요소를 변경할 수 있음.
# list[0] = '김구'
# list[1] = '90'
# print(list)

# True - False로 // 42.195 - 31.4 // hello - hi // 30 -20
# list3[0] = False
# list3[2] = 31.4
# list3[-1] = "Hi"
# list3[1] = 20
# print(list3)

#  슬라이싱 - 리스트 자르기
num = [0,1,2,3,4,5,6,7]
# print(num[1:])

str1 = ['a','b','c','d','e','f']
# print(str1[2:4])
# print(str1[1:])
# print(str1[:3])
# print(str1[:])
# print(str1[1:-1])


# 리스트 길이 len 
# print(list1, len(list1))
# print(list2, len(list2))
# print(list3, len(list3))
# print(len(list1[1]))            #리스트 내 리스트 길이는 인덱싱하면 된다.


# 리스트 값 추가 - append
# num.append(8)
# print(num)

# str1.append('ㄱ')
# str1.append('ㄴ')
# str1.append('ㄷ')
# str1.append([1,2,3])
# print(str1)


# 리스트에서 특정 값 삭제 - remove
# str1.remove('a')
# str1.remove('c')
# str1.remove('f')
# print(str1)

# 리스트 내 요소 확인 -in // not in
# print(1 in num)
# print(2 not in num)

# lan = ['영어','한국어','일본어','스페인어','중국어']
# print('영어' in lan)
# print('한글' not in lan)

# if '일본어' in lan :
#     print('일본어가 있습니다.')

tmp = [
    ['미국','영국','일본','중국','스페인'],
    ['영어','영어','일본어','중국어','스페인어']
]
# print(tmp[1][2])
# tmp[0][-2] = '대만'
# print(tmp)
# print(tmp[0][2:])
# tmp[0].append('프랑스')
# tmp[1].append('프랑스어')
# print(tmp)
