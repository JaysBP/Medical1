from random import *

n1 = randrange(1,10)
n2 = randrange(10)
n3 = randint(1,10)

print(n1,n2,n3)

lotto = []
# 랜덤한 수 6개를 넣으시오.

for i in range(6) :
    l = randint(1,45)
    lotto.append(l)
print(lotto)


mynum = []
for i in range(6) :
    m = int(input("숫자를 입력하세요 >>"))
    mynum.append(m)
print(mynum)