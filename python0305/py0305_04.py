a = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
value = 1
for i in range(0,5) :
    for j in range(0,5) :
        a[i][j] = value
        value += 1
        
#  좌표를 입력하면 촤표를 0으로 변경하는 프로그램 구현

while True :
    print(0," ㅣ ",0,1,2,3,4,sep='\t')
    print('-' * 50)
    for i in range(0,5) :
        print(i,"\t","ㅣ",end='\t')
        for j in range(0,5) :
            print(a[i][j], end='\t')
        print()
    x = int(input("X좌표 값을 입력하세요 >>"))
    y = int(input("Y좌표 값을 입력하세요 >>"))
    # 입력된 좌표값이 0으로 변경
    a[x][y] = "X"
