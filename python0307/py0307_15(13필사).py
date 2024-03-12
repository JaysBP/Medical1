# 크기가 10인 리스트를 생성하는데, 7개는 0으로, 3개는 1로 채우세요
list = [0] * 10
# print(list)
for i in range(3) :
    list[i] = 1
# print(list)

# 1. 크기가 100인 리스트 생성, 10개는 1로 채워라. 단, 랜덤으로 섞어서 출력해라
import random
alist = [0 for i in range(100)]
for i in range(10) :
    alist[i] = 1
random.shuffle(alist)
# print(alist)

# 2. 10X10 형태의 2차원 배열에 넣어라.
blist = []
blists = []
for i, j in enumerate(alist) :
    if (i+1) % 10 == 0 :
        blist.append(j)
        blists.append(blist)
        blist = []
    else :
        blist.append(j)        
# print(blists)

# 3. 새로운 리스트 추가로 생성   
newlist = [["추첨"]*10 for _ in range(10)]
