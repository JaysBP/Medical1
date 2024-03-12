# # 반복문 for
# '''
# for 변수 in 반복가능데이터
#     수행할 문장
# '''
# # 순차적으로 커질 때 range를 사용(시작값,끝값+1,증가값)
# for i in range(0,5,1) :
#     print('안녕')
    
# # 증가값이 1인 경우 생략 가능
# for i in range(0,5) :
#     print('안녕')
    
# # n번 반복할 경우 range(n)으로 사용 가능
# for i in range(4) :
#     print('안녕')
    
# # i를 쓰지 않고 언더바(_)로도 활용 가능하다.
# for _ in range(2) :
#     print('반갑습니다.')

# # 단순히 5회 반복을 시킨 것
# for i in range(5) :
#     num = int(input("숫자를 입력하세요 >>"))
#     print('입력하신 숫자는 : {}'.format(num))

# 반복문 내에서 사용하는 i or j는 카운터 변수라고 부른다.
#   -> 반복실행될 때마다 현재 실행횟수에 해당하는 숫자가 들어감, 가장 처음은 실행 전이라 0이 됨

# for i in range(10):
#     print(i)                # 0부터 시작(첫 시작은 0이라서) ~ 열번째인 9까지 결과값 확인
    
    
# str1 = '안녕하세요'
# for i in str1 :
#     print(i)

# # 1부터 15까지 출력하라
# for i in range(1,16):
#     print(i)
    
# # 10을 반복해서 4번 출력하라
# for i in range(4):
#     print(10)
    
# # HelloWorld를 6번 반복해서 출력하라
# for i in range(6) :
#     print("Hello World")
    
# # 1-100 사이의 2의 배수를 출력하라
# for i in range(2,101,2):
#     print(i, end=' ')                   #( , end=' ')를 붙여주면 이어져서 볼 수 있음.

# # 1-100 사이의 5의 배수를 출력하라
# for i in range(5,101,5) :
#     print(i)