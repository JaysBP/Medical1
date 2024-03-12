import random

a = []
# 1- 25까지의 숫자를 리스트에 넣기 
for i in range(0,25) :
    a.append(i+1)

# print(a)
# 리스트 랜덤으로 섞기
random.shuffle(a)
# 2차원 리스트에 랜덤으로 섞은 숫자 넣기
arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(0,5) :
    for j in range(0,5) :
        arr[i][j] = a[(5 * i)+j]


# 출력
while True :
    print('-' * 50)
    print('[좌표맞추기 프로그램]')
    print('-' * 50)
    print('순번','ㅣ',0,1,2,3,4,sep="\t")
    print('-' * 50)
    for i in range(0,5) :
        print(i,"\t","ㅣ",end='\t')
        for j in range(0,5) :
            print(arr[i][j],end='\t')
        print()
    print('-' * 50)
        
# 좌표 맞추기 게임 만들기 ..
    x = int(input('X좌표 값을 입력하세요 >>'))
    y = int(input("Y좌표 값을 입력하세요 >>"))
    arr[x][y] = "X"