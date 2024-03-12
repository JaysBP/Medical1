# 5x5 배열의 2차원 리스트를 0으로 채워서 출력하라
# 1차원으로 25개 만들고 2차원으로 변경, 5x5로 만들고
# list = [0 for i in range(25)]
import random
list = [[0] for i in range(25)]
for i in range(5) :
    list[i] = 1
random.shuffle(list)
# print(list)
# 4. 5*5 2차원 리스트에 넣기
checklist = [[0]*5 for i in range(5)]
for i in range(5) :
    for j in range(5) :
        checklist[i][j] : list[5*i+1]
print(list)

# 추첨 5*5 2차원 배열
viewlist = [['추첨']*5 for i in range(5)]
c_count = 1
answer_count = 0
coodinated = []
while True :
    print("\t[5x5 checklist좌표]")
    print("-" * 60)
    print("",0,1,2,3,4,sep='\t')
    print("-" * 60)
    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(checklist[i][j],end='\t')
        print()
    print("-" * 60)
    
# 5. viewList 출력
    print("\t[5x5 viewlist좌표]")
    print("-" * 60)
    print("",0,1,2,3,4,sep='\t')
    print("-" * 60)
    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(viewlist[i][j],end='\t')
        print()
    print("-" * 60)

# 7. 좌표입력후 확인
    print("[ 현재 도전횟수 : {} 번 ]".format(c_count))
    x = int(input("가로 좌표를 입력하세요.>> "))
    y = int(input("세로 좌표를 입력하세요.>> "))
    if checklist[x][y] == 1:
        viewlist[x][y] = "당첨"
        answer_count += 1
    else:
        viewlist[x][y] = "[꽝]"
        
    # 입력한 좌표값을 coodinate에 넣기
    coodinated.append([x,y])
    # 5개의 당첨을 맞추면 프로그램 종료
    if answer_count==5:
        print("[ 모두 정답 확인 ]")
        print("프로그램을 종료합니다.")
        break
    # 10번 시도후 프로그램 종료        
    c_count += 1    
    if c_count==10:
        print("[ 모두 도전 종료 ]")
        print("프로그램을 종료합니다.")
        break
print(f"입력하신 좌표는 모두 {coodinated}입니다.")
