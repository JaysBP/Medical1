# 반복문 for // while문
'''
for i in range(시작,끝+1,증감값) :
    수행할 문장
    
while 조건식 :
    실행할 문장
    
변수 = 시작값       ex) i = 0
while 변수 < 끝값 :     - 조건이 참일 때만 반복
    반복구문
    변수 = 변수 + 증가값    ex) i = i + 1

'''
# # for문으로 '안녕하세요' 3번 출력
# for i in range(3) :
#     print("안녕하세요")
# # while문으로 '안녕하세요' 3번 출력 - 변수 만들고, 조건문 쓰고, 무한대 증가하지 않게 조건 하나 더 작성
# i = 0
# while i < 3 :
#     print('안녕하세요')
#     i = i + 1

# # 예제 1) for/while문으로 0-10까지 출력
# # 1) for문
# for i in range(0,11,1) :
#     print(i,end=' ')
# # 2) while문
# i = 0
# while i < 11 :
#     print(i,end=' ')
#     i = i+1

# # 예제 2) while을 사용하여 1 - 10 사이의 3의 배수를 출력하라 // 1-100사이의 홀수만 출력
# i = 1
# while i < 11 :
#     if i % 3 == 0 :
#         print(i,end=' ')
#     i = i + 1
    
# j = 0
# while j < 101 :
#     if j % 2 == 1 :
#         print(j,end=' ')
#     j = j + 1

# i = 1
# sum = 0
# while i < 101 :
#     sum += i
#     i += 1
# print(sum)

# while 조건문이 참일 경우 무한반복 -> while True는 무조건 참이기 때문에 무한반복됨.
# 조건문을 필히 만들어줘야 함.


# # break문 / continue문을 사용해야 한다.
# # break문 - 반복문을 빠져나와 다음 단계를 수행한다.
# n = 0
# while n < 100 :
#     print(n,end=' ')
#     if n == 4 :
#         break
#     n = n + 1
    
# # break문 예제 ) 
# breakletter = input("중단할 문자를 입력하세요 >>")
# for  letter in 'python' :
#     if letter == breakletter :
#         break
#     print(letter)
    
    
# while True :
#     n = input("숫자를 입력해주세요(종료:0)")
#     print(n)
#     if n == '1':
#         print("종료되었습니다.")
#         break


# # continue문 - 반복문에서 남은 문장을 수행하지 않고 다음 단계로 넘어감
# n =0
# while n < 100 :
#     n += 1
#     if n%2 == 0:
#         continue                # 상위 조건에 대해 부합하면 아래 문장을 실행하지 않고 다시 반복문 상부로 올라감.
#     print(n,end=' ')

# # break는 문자를 만나면 프로그램(반복문)이 종료되는데, continue는 해당 문자를 제외하고(건너뛰고) 다시 반복문이 실행됨.