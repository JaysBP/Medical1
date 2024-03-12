#  Day 5 복습
'''
변수 - bool, int, float, str (참or거짓, 정수, 실수, 문자열)

input() - 입력을 받음. 콘솔 창에서 직접 입력
- input을 사용할 때에 변수를 통해 입력한 값을 저장 

if문 - 조건문 형태로 만들어서 해당할 때에 실행문으로 넘어가도록 함. - 조건문이 참일 때만 실행문으로 넘어감.
- elif, else는 생략 가능, if문 건너뛸 때는 pass 사용
- 다중 if문 : 최초 if가 참인 조건을 건 후에 다시 if문을 통해 진행될 수 있도록 함. 

for 반복문 - 무조건적인 반복
for 변수 in 반복가능한 데이터 -> 순차적으로 커질 때에는 range 사용 // for i in range(0,10,1) : (시작값, 끝값+1, 증감값)
                                                                  for i in range(5) : i가 0부터 4까지 반복해라 -> 5번 반복해라.

ex) a = 10 b = '안녕하세요' -> for i in range(5) : // print(a) print(b) => 5번씩 반복을 위한 명령어


'''
# a = 10
# b = '안녕하세요'

# for i in range(5) :
#     # print(i)
#     a = a+1
#     print(a)
#     print(b)

#  입력 - 이름 점수 5명
# 60점 이상은 합격, 미만은 불합격으로 출력
#  출력 형태는 [ OOO님 합격/불합격 입니다. ]

# for i in range(5) :
#     n = input("이름을 입력하세요 >>")
#     s = int(input("점수를 입력하세요 >>"))
#     if s >= 60 :
#         print("[{}님 합격입니다.]".format(n))
#     else :
#         print("[{}님 불합격입니다.]".format(n))

'''
list - 변수명을 지정한 후 요소를 입력하여 하나의 형태로 만든 것.
모든 타입의 변수가 포함 가능- bool, str, int, float
fruit = ['딸기','사과','배','포도','한라봉'] -> f1=fruit[1] 선택가능한 요소에 대한 접근, 확인, 추가, 삭제, 대체 모두 가능
추가 - append   // 확인 - in or not in  // 

'''

# for n in [100,200,300,400,500] :
#     print(n)                            # 리스트 명을 작성해도 가능함.
    
# for i in range(len(fruit)) :            # 리스트의 길이만큼 i를 1씩 증가하라
#     print(i)
#     print(fruit[i])
    
# num = [[1,2,3],[4,5,6],[7,8,9]]
# print(num[0][0],num[1][0],num[2][0])

# for i in range(len(num)) :
#     print(num[i][0])



