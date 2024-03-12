# from random import *

# # 1 - 45까지의 숫자를 두 가지 방법으로 리스트에 넣어라 (입력받는 버젼, 랜덤하게 넣는 버젼)
# lotto = []
# mynum = []

# # 1) 입력한 수 리스트 형성
# for i in range(6) :
#     m = int(input("{}번째로 원하는 숫자를 입력하세요 >>".format(i+1)))
#     mynum.append(m)
# print(mynum)

# #  2) 랜덤한 숫자 리스트 형성
# l = []
# for i in range(1,46) :
#     l.append(i)
# # print(l)
# for i in range(100) :
#     m = randint(0,44)
#     l[0], l[m] =  l[m], l[0]
# # print(lotto)
# for i in range(6) :
#     lotto.append(l[i])
# print(lotto)

# ok = []
# for i in range(6) :
#     if mynum[i] in lotto :
#       ok.append(mynum[i])
# print(ok)



from random import*
mynum = []
lotto = []

# 1)
for i in range(6) :
    m = int(input("원하는 숫자를 입력하세요>>"))
    mynum.append(m)
print(mynum)

# 2)
l = []
for i in range(1,46):
    l.append(i)
# print(l)
for i in range(100) :
    t = randint(0,44)
    l[0], l[t] = l[t], l[0]
    # print(l)
for i in range(6) :
     lotto.append(l[i])
print(lotto)