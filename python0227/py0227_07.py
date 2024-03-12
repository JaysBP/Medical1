# print("2단 출력")
# for i in range(1,10) :
#     print("2 * {} = {}".format(i,2*i))
    
# 원하는 수를 입력받아 구구단을 입력하라. 
for _ in range(5) :
    n = int(input("원하는 수를 입력하시오 >>")) 
    for i in range(1,10) :
        print("{} * {} = {}".format(n,i,n*i))