# 함수선언 - 두 수를 입력받아 입력한 사이의 합계를 구하라
def cal(num1,num2) :
    if num1 > num2 :
        num1,num2 = num2,num1
    sum = 0
    for i in range(num1,num2+1,1):
    #    print(i)
        sum += i             # for문 돌린 거에 sum을 i로 받아서 적용 후 아래 리턴으로 내려준다
    return sum

num1 = int(input("첫번째 숫자를 입력하세요 >>"))
num2 = int(input("두번째 숫자를 입력하세요 >>"))

sum = 0
sum = cal(num1,num2)

print("합계 : ",sum)