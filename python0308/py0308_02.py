card_list = []
shape_list = ['spade' , 'diamond' , 'heart' , 'clover']
num_list = [0]*13

for i in range(1,14) :
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
    
# print(shape_list)
# print(num_list)

# 카드 한 세트를 구현하여 출력하라
import random
count = 0
card_list = [[0] * 2 for i in range(52)]
for i in shape_list :
    for j in range(13) :
        card_list[count] = [i,num_list[j]]
        # print(card_list)
        count += 1  
  
random.shuffle(card_list)
array_num = 0
# print(card_list)      
while True :
    # 카드 출력
    print(f"현재 카드는 {len(card_list)-array_num}장 남았습니다.")
    c_num = int(input("카드를 몇 개 선택하시겠습니까?(1.1장//2.5장//0.종료) >>"))
    if c_num == 1 :
        print(card_list[array_num])
        array_num += 1
    elif c_num == 2 :
        for i in range(5) :
            print(card_list[array_num],end=' ')
            array_num += 1
    elif c_num == 0 :
        print("카드 출력을 종료합니다.")
        break