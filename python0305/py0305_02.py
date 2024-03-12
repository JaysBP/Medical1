# 리스트에 1부터 25까지 숫자를 넣으세요
# a = [] 
# for i in range(0,25) :
#     i += 1
#     print(i,end=' ')
    
# [[1,2,3,4,5],[6,7,8,9,10],,,,[21,22,23,24,25]] 형태 만들기
a = []
a_i = []
for i in range(0,25) :
    if (i+1) % 5 == 0 :
        a_i.append(i+1)
        a.append(a_i)
        a_i = []
    else :
        a_i.append(i+1)
print(a)