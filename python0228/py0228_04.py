# a, b = 10, 8 
# a, b = b, a

n1 = [0,1,2,3,4,5]
# n1[0], n1[3] = n1[3], n1[0]
# print(n1)
# n1[2], n1[5] = n1[5],n1[2]
# print(n1)

con = ['미국','영국','일본','중국','스페인']
# con[1], con[3] = con[3],con[1]
# print(con)

# 리스트 내 요소 랜덤으로 섞기
from random import *
n1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(100) :
    a = randint(0,9)            # 랜덤 인덱스 생성
    n1[0],n1[a] = n1[a],n1[0]   # 숫자 서로 섞음
    print(n1)