# 크기가 10인 리스트를 생성하는데, 7개는 0으로, 3개는 1로 채우세요

# list = []
# count = 0
# for i in range(0,10) :
#     if i < 7 :
#         i = 0
#     else :
#         i = 1
#     list.append(i)
# print(list)

# list = [0] * 10
# for i in range(3) :
#     list[i] = 1
# print(list)

# 1. 크기가 100인 리스트 생성, 10개는 1로 채워라. 단, 랜덤으로 섞어서 출력해라
import random

# list2 = [0] * 100
# for i in range(10) :
#     list2[i] = 10
#     random.shuffle(list2)
# print(list2)

alist = [0 for i in range(100)]
for i in range(10) :
    alist[i] = 1
random.shuffle(alist)
# print(alist)

# 2. 10X10 형태의 2차원 배열에 넣어라.
blist = []
blists = []
for i,j in enumerate(alist) :
    if (i+1) % 10 == 0 :
        blist.append(j)
        blists.append(blist)
        blist = []
    else :
        blist.append(j)
        
# 3. 새로운 리스트 추가로 생성   
newlists = [["추첨"]*10 for _ in range(10)]

count = 0
while True:
    print("[ 10*10 좌표 ]")
    print("-"*60)
    #print(blists)
    print("",0,1,2,3,4,5,6,7,8,9,sep="     ")
    print("-"*60)
    for i,b in enumerate(newlists):
        print(i,end="  ")
        for bb in b:
            print(bb,end="  ")
        print()
    print("-"*60)
    x = int(input("가로 좌표를 입력하세요."))
    y = int(input("세로 좌표를 입력하세요."))
    # bLists - 값을 비교, newlists - 표시
    if blists[x][y] == 1: #당첨
        newlists[x][y] = "[당첨]"
        print(f"{count+1}회 도전 끝에 당첨입니다. 축하합니다!")
        break
    else: # 꽝
        newlists[x][y] = "[꽝]"
        count += 1
        if count > 9 :
            print("열번의 기회가 모두 끝났습니다.")
            break