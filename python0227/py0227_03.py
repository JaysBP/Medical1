#  0 - 20 사이 5의 배수로 이뤄진 리스트 출력
# num = []
# for i in range(0,21,5) :
#     print(i,end=' ')
#     num.append(i)
# # num.append(5)
# # num.append(10)
# # num.append(15)
# # num.append(20)
#     print(num)  

# # 방법 1)

# for i in range(21):
#     if i % 5 == 0:
#         num.append(i)
# print(num)

lan = ['c','python','java','jquery','css']
# 1. 하나하나 출력 // 2. 줄바꿈 형태로 1. -- 2. -- 출력
# 방법 1)
# for a in lan :
#     print(a,end=' ')
# for i in range(len(lan)) :
#     print(lan[i])
    
# 방법 2)
# for i in range(1) :
#     print(" 1.{}\n 2.{}\n 3.{}\n 4.{}\n 5.{}".format(lan[0],lan[1],lan[2],lan[3],lan[4]))
    
# for i in range(5) :
#     print('{}. {}'.format(i+1,lan[i]))


num = [1,-1,2,3,-4,5,6,-8,9,-10]        # 양수면 양수, 음수면 음수라고 구분

for i in num :
    if i > 0 :
        print("{}: 양수".format(i))
    else :
        print("{}: 음수".format(i))
        
for i in range(num[i]) :
    if i > 0 :
        print("{}: 양수".format(i))
    else :
        print("{}: 음수".format(i))