# # 숫자 1개를 입력받아 출력하라.
# # 1. 숫자 1개 입력 // 2. 숫자 1개 출력
# num = int(input("숫자를 입력하시오 >>"))
# print(num)

# # 숫자 2개를 입력받아 출력하라.
# # 1. 숫자 2개 입력 // 2. 숫자 2개 출력
# num1 = int(input("첫번째 숫자를 입력하시오 >>"))
# num2 = int(input('두번째 숫자를 입력하시오 >>'))
# print(num1 + num2)

# 숫자 5개를 입력받아 출력하라.
# 1. 숫자 5개 입력 // 2. 숫자 5개 출력
nums = []
for i in range(0,5) :
    n = int(input("숫자를 입력하세요 >>"))
    nums.append(n)      # 아예 append에 n 자체를 넣어도 가능.
    
sum = 0                 # 먼저 변수를 선택한 뒤에
for num in nums :
    sum += num          # 반복문 작성하고 반복될 수 있게 작성
print('합계 : ',sum)