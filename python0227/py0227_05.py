# 1 - 5까지의 합계를 구하라
# sum = 1+2+3+4+5
# print(sum)
# total = 0
# total = total + 1
# total = total + 2
# total = total + 3
# total = total + 4
# total = total + 5
# print(total)
# t = 0
# for i in range(1,6,1) :
#     t = t + i
# print(t)

# 1 - 10까지의 합을 구하라 for문 사용
# a = 0
# for i in range(1,11) :
#     a += i
# print(a)

# b = 0
# for i in range(1,101) :
#     b += i
# print(b)

# 첫번째 입력한 수부터 두번째 입력한 수까지의 합을 구하라.
k = 0
n1 = int(input('첫번째 숫자를 입력하시오 >>'))
n2 = int(input("두번째 숫자를 입력하시오 >>"))

for i in range(n1,n2+1) :
    k += i
print(k)