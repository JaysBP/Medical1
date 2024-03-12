

''' 반복문 - for , while
for 변수 in 반복 가능한 데이터
    수행문

for 카운터변수 in range(시작값,끝값+1,증감값) :
   
'''

# for i in range(0,10,1):
#     print('수행문입니다.')
# print('-'*80)
    
# for i in range(0,3):
#     print('두번째 수행문입니다.')
# print('-'*80)
# for i in range(5) :
#     print('세번째 수행문입니다.')
# print('-'*80)
# for _ in range(7):
#     print('안녕하세요!')
# print('-'*80)

# for i in range(10,0,-2):
#     print(i,'증감 2: 수행문입니다.')    
# print('-'*80)

'''
for 변수 in 리스트명 :
    실행문
    
for 변수 in range(len(리스트명)) :
    실행문
    리스트명[변수]
'''
# l1 = [100,200,300,400,500]
# for a in l1 :
#     print(a)
    
# for i in range(len(l1)):
#     print(l1[i])

# for문을 사용하여 1-100 사이의 홀수를 출력하라 1) if문 미사용 2) if문 사용
# for i in range(1,101,2):
#     print(i,end=' ')
  
# for i in range(101):
#     if i % 2 == 1 :
#         print(i,end=' ')
        
# for i in range(50,2,-6):
#     print(i-2,end=' ')
    
# for i in range(48,1,-6):
#     if i % 6 == 0 :
#         print(i,end=' ')

# input 사용, 입력-두 수를 입력받아 // 사칙연산을 출력하라
# n1 = int(input("첫번째 숫자를 입력하세요 >>"))
# n2 = int(input("두번째 숫자를 입력하세요 >>"))
# c = input("선택하실 연산을 입력해주세요 >>")

for i in range(10):
    n1 = int(input("첫번째 숫자를 입력하세요 >>"))
    c = input("선택하실 연산을 입력하세요 >>")
    n2 = int(input("두번째 숫자를 입력하세요 >>"))
#     # print("{} + {} = {}".format(n1,n2,n1+n2))
#     # print("{} - {} = {}".format(n1,n2,n1-n2))
#     # print("{} * {} = {}".format(n1,n2,n1*n2))
#     # print("{} / {} = {:.2f}".format(n1,n2,n1/n2))
    if c == "+" :
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif c == "-" :
        print('{} - {} = {}'.format(n1,n2,n1-n2))
    elif c == "*" :
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    elif c == "/" :
        print('{} / {} = {:.2f}'.format(n1,n2,n1/n2))
    else :
        print('잘못된 연산입니다.')