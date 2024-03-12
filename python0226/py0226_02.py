# Day 3 복습 예제 1) 조건문 활용
# 나이가 10살 이상, 키 150cm 이상만 탑승 가능
# age = int(input("나이를 입력하세요 >>"))
# height = int(input("키를 입력하세요 >>"))

# if age >= 10 and height >= 150 :
#     print("탑승 가능합니다.")
# else :
#     print("탑승할 수 없습니다.")
    
# # Day 3 복습 예제 2) 변수 출력
# 숫자 3개(정수)를 입력받은 후 연산 1개를 입력받아 a+b+c=d의 형태로 출력하기

# no1 = int(input("첫번째 숫자를 입력하세요 >>"))
# no2 = int(input("두번째 숫자를 입력하세요 >>"))
# no3 = int(input("세번째 숫자를 입력하세요 >>"))

# k = input("연산에 사용될 부호를 입력하세요 >>")

# if k == '+' :
#     print("{} {} {} {} {} {} {}".format(no1,k,no2,k,no3,'=',(no1+no2+no3)))
# elif k == '-' :
#     print("{} {} {} {} {} {} {}".format(no1,k,no2,k,no3,'=',(no1-no2-no3)))
# elif k == '*' :
#     print("{} {} {} {} {} {} {}".format(no1,k,no2,k,no3,'=',(no1*no2*no3)))
# elif k == '/' :
#     print("{} {} {} {} {} {} {:.2f}".format(no1,k,no2,k,no3,'=',(no1/no2/no3)))
    
# else :
#     print("부호가 올바르지 않습니다. 다시 작성해주시길 바랍니다.")