#  Day 6 복습
'''
반복문 - for문
(기본형태)
for 변수 in 반복가능한데이터 :
    수행문장
    
(리스트 사용 시)
for 요소 in 리스트명 :
    반복할 실행문

(range 사용 시) - 실행문이 i가 시작값부터 끝값까지 반복
for i in range(시작값, 끝값+1, 증감값) :
    반복할 실행문

(이중 for문) - 반복수 1 * 반복수 2
for i in range(반복수 1) :
    실행문 1
    for j in range(반복수 2) :
        실행문 2

ex)
for i in range(5) :
    print('i =' , i) -> 5번 반복 : i=0,.,1,2,3,4
    print('-'* 50) 
    for j in range(3) -> 3번 반복 : j=0,1,2
        print('j =', j)
        
// 구구단 출력 //
for i in range(1,10) :                          -) 단순히 2단만 출력
    print('{} * {} = {}'.format(2,i,2*i))
    
for i in range(2,10) :                          -> 2-9단까지 출력
    for j in range(1,10) :
        print('{} * {} = {}'.format(i,j,i*j))
    print()                                     -> 줄바꿈 표시

(구구단 세로방향으로 진행)
for i in range(2,10) :
    print('{}단'.format(i),end='\t')
for i in range(1,10) :
    # 줄이 바뀔 때마다 
    for j in range(2,9) :
        # 요소가 출력될 때마다
        print('{} * {} = {}'.format(j,i,i*j),end='\t')    -> 세로방향으로 하기 위해서 단과 곱셈을 반대로
        


// 리스트 형태 // - [요소1,요소2,요소3.........요소n]
fruit = ['딸기','사과','배','수박','귤']
#     i =  0      1     2    3     4

리스트 요소 추가 : append /// 리스트 요소 삭제 : remove or del /// 리스트 요소 확인 : in or not in
(리스트명 사용)
for i in fruit :
    print(i)
(range 사용)
for i in range(len(fruit)) :
    print(fruit[i])
    
num =[[10,20,30],[100,200,300],[1,2,3]]
for n in num :
    print(n)                                - 리스트 내 전체 요소를 보여줌, 따로 분리는 안 됨.

for n in num :
    for a in n :
        print(a)                            - for문을 이중으로 사용하여 리스트 내 요소를 따로 분리해서 하나씩 출력
        

for i in range(len(num)) :
    for j in range(len(num[i])) :
        print(num[i])                       - 최초 for문에서 다음 for문에서는 요소를 추가해서 넣고 출력 시에도 두번째 for문에 있는 문장과 동일하게
        
        
(리스트에 숫자 넣을 때 한 줄로 표현하기)
## [표현식 for 항목 in 리스트 if 조건문]
(1번)
aa = []
for i in range(1,11) :
    aa.apend(i)
print(aa)                                   [1,2,3,4,5,6,7,8,9,10]
                                            - 1번 = 2번  동일함 -> 한 문장으로 만들 수 있다는 장점. 리스트 내에 숫자를 채운다.
(2번)
a = [i for i in range(1,11)] :
print(a)                                    [1,2,3,4,5,6,7,8,9,10]

ex)
b = [i for i in range(1,11)]                [1,2,3,4,5,6,7,8,9,10]
c = [i+1 for i in b]                        [2,3,4,5,6,7,8,9,10,11]


# names = ['홍길동','유관순','이순신','강감찬','김구']

# (넘버링 가로출력)
#  방법 1) - range 사용해서 넘버링
# for i in range(len(names)) :
#     # print(names[i],end=' ')
#     print('{}.{}'.format(i+1,names[i]),end=' ')

#  방법 2) 변수 하나를 더 추가해서 넘버링
# a= 0
# for i in names :
#     a = a + 1
#     # print(i,end=' ')
#     print('{}.{}'.format(a,i))

(추가 - enumarate 사용  : 추후에 확인)
for i, name in enumerate(names):
    print('{}.{}'.format(i+1,name))
    
for i, name in enumerate(names, start = 1):
print('{}.{}'.format(i+1,name))
'''

