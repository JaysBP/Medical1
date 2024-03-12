import random
# 1. 0으로 25개 1차원 리스트 생성
alist = [0] * 25

# 2. 1로 5개를 변경
for i in range(5) :
    alist[i] = 1
    
# 3. 랜덤섞기
random.shuffle(alist)
# print(alist)

# 4. 5*5 2차원 리스트에 넣기
checklist = [[0]*5 for i in range(5)]
for i in range(5) :
    for j in range(5) :
        checklist[i][j] = alist[5*i+j]
        
# 추첨 5*5 2차원 배열
viewlist = [['추첨']*5 for i in range(5)]
check_count = 1
answer_count = 0
while True :
    
    # 5. checkList 출력
    print("\t[5x5 checklist 좌표]")
    print("-" * 60)
    print("",0,1,2,3,4,sep="\t")
    print("-" * 60)
    for i in range(5) :
        print(i,end="\t")
        for j in range(5) :
            print(checklist[i][j],end='\t')
        print()
    print("-" * 60)
    
    # 6. viewList 출력
    print("\t[5x5 viewlist 좌표]")
    print("-" * 60)
    print("",0,1,2,3,4,sep="\t")
    print("-" * 60)
    for i in range(5) :
        print(i,end="\t")
        for j in range(5) :
            print(viewlist[i][j],end='\t')
        print()
    print("-" * 60)
    
    # 7. 좌표입력후 확인
