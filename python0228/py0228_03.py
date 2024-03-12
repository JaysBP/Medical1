from random import *

# n1 = randrange(1,11)
# n2 = randint(1,10)

#  랜덤한 숫자 6개를 lotto리스트에 넣고 내가 입력한 숫자 6개는 mynum 리스트에 넣어라

lotto = []
mynum = []

# n1 = randint(1,10)
# n2 = randint(1,10)
# n3 = randint(10,25)
# n4 = randint(10,25)
# n5 = randint(25,40)
# n6 = randint(25,40)
for i in range(6) :
    n = randint(1,45)
    if n not in lotto :
        lotto.append(n)
print(lotto)
# for i in range(6) :
#     n = int(input("{}번째로 원하시는 숫자를 입력하세요 >>".format(i+1)))
#     mynum.append(n)
# print(mynum)