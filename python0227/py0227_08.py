num = [i for i in range(1,11)]
# for 문을 사용하여 1-10까지 숫자를 채워라
n = 0
for i in range(11) :
    num.append(i)    
    
num2 = []
# 1 - 10까지의 수 중 짝주는 num2 리스트에 넣어라
for i in range(1,11) :
    if i % 2 == 0  :
        num2.append(i)
        
num = [1,2,3,4,5,6,7,8,9,10]
# num리스트를 사용하여 1~10까지의 합을 구하라
# n = 0
# for _ in num :
#     for i in range(1,10) :
#         n += 1
#     print(n)

for n in num :
    print(n, end=' ')
print()

a = 0
for n in num :
    a += n
print(a)


b = 0
for i in range(len(num)):
    b = b + num[i]
c = 0
for n in num2 :
    c = c + n
    print(n,end=' ')
d = 0
for i in range(len(num)):
    d = d+num[i]
print(d)