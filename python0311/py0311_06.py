# def plus(v1,v2) :           # 함수선언
#     result = 0
#     result = v1 + v2
#     return result           # 위 함수를 아래에 불러온 곳으로 전해줌.    
#                             # 함수호출

# print(plus(100,200))
# print("프로그램 종료")


# def calc(v1,v2,op) :
#     result = 0                  # 지역변수
#     if op == "1" :
#         result = v1+v2
#     elif op == "2" :
#         result = v1-v2
#     elif op == "3" :
#         result = v1*v2
#     elif op == '4' :
#         result(v1/v2)
    
#     return result
# aaa = 0  
# print("1.더하기//2.빼기//3.곱하기//4.나누기")
# a_input = input("계산하실 연산이호를 입력하세요 >>")
# var1 = int(input("첫번째로 입력할 숫자를 작성하세요 >>"))
# var2 = int(input("두번째로 입력할 숫자를 작성하세요 >>"))

# data = calc(var1,var2,a_input)

# print("결과값 :",data)

# def plus(v1,v2) :
#     v1 = 100
#     v2 = 200
#     return v1,v2     

# v1 = 1
# v2 = 2
# v1,v2 = plus(v1,v2)

# print(v1,v2)

def cal(a_input1, b_input1) :
    result1 = a_input1+b_input1
    result2 = a_input1-b_input1
    result3 = a_input1*b_input1
    result4 = a_input1/b_input1
    return result1,result2,result3,result4

a_input1 =int(input("첫번째 숫자를 입력하세요"))
b_input1 =int(input("두번째 숫자를 입력하세요"))

result1,result2,result3,result4 = cal(a_input1,b_input1)
data = cal(a_input1,b_input1)
print("결과값 :",result1,result2,result3,result4)
print('결과값 :', data)