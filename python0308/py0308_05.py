# [['spade', 2], ['diamond', 5], ['heart', 8], ['diamond', 'A'], ['spade', 10], ['diamond', 'K'], ['clover', 4], ['spade', 5], ['heart', 'Q'], 
#  ['diamond', 2], ['diamond', 4], ['heart', 7], ['clover', 'A'], ['diamond', 7], ['heart', 'A'],['spade', 6], ['diamond', 6], ['clover', 8], ['spade', 8], ['heart', 'J'], ['diamond', 'J'],
#  ['diamond', 'Q'], ['clover', 7], ['spade', 9],['spade', 3], ['heart', 4], ['clover',10], ['clover', 5], ['spade', 7], ['spade', 'J'],['spade', 'A'], ['heart', 6], ['diamond', 8], 
#  ['heart', 2], ['heart', 5], ['diamond', 9], ['diamond', 3], ['heart',3], ['clover', 9], ['clover', 'Q'],['clover', 2], ['heart', 'K'],['diamond', 10], ['spade', 'K'],
#  ['spade', 'Q'], ['clover', 3],['spade', 4], ['heart', 9],['clover', 'K'], ['clover', 6], ['heart', 10], ['clover', 'J']]
import random
card_list = []
shape_list = ['spade' , 'diamond' , 'heart' , 'clover']
num_list = [0]*13

for i in range(1,14) :
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"

card_list = [[0] * 2 for i in range(52)]
count = 0
for i in shape_list :
    for j in range(13) :
        card_list[count] = {"shape" : i, "num" : num_list[j]}
        count += 1  
random.shuffle(card_list)
# print(card_list)

array_num = 0
while True :
    print(f"현재 카드는 {len(card_list)-array_num}장 남았습니다.")
    select = int(input("뽑으려는 카드의 수를 입력하세요.(1.1장//2.5장//0.취소) >>"))
    if select == 1 :
        print(card_list[array_num])
        array_num += 1
    elif select == 2 :
        for i in range(5) :
            print(card_list[array_num])
            array_num += 1
    elif select == 0 :
        print('선택이 취소되었습니다.')
        break