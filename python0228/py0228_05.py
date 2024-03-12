from random import *

#  1. 변수선언
lotto = []
mynum = []

#  2. 입력받은 수를 mynum 리스트 내에 추가하라.

#  3. 로또 번호 생성기
l = [1,2,3,4,5,6,7,8,9,10]
for i in range(50) :
    a = randint(0,9)                # 0번부터 9번까지 랜덤한 숫자 생성
    l[0], l[a] = l[a],l[0]
print(l)

for i in range(6) :
    lotto.append(l[i])
print(lotto)