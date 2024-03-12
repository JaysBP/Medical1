# # continue 예제 1) 1 - 100까지의 합에서 3의 배수는 제외하고 출력하고 그 값을 모두 더하라
# i = 0
# sum = 0
# while i < 100 :
#     # print(i,end=' ')
#     i += 1
#     if i % 3 == 0 :
#         continue
#     sum += i
# print(sum)


# # 랜덤한 숫자를 만들어서 내가 입력한 값이 랜덤한 숫자와 같으면 당첨, 아니면 다시 입력해주세요 출력
# # 입력한 숫자가 랜덤숫자보다 작으면 작습니다. 더 큰 수를 입력하세요 // 크면 큽니다 더 작은 수를 입력하세요 출력
# # 현재 입력한 숫자 모두를 inputlist에 넣으시오.
# # 10회 도전 후 프로그램이 자동으로 종료될 수 있게 하시오
# # 10회 도전이 끝난 후에 랜덤숫자 알려주기

from random import *
inputlist = []
a = randint(1,100)
k = 0
while k < 10 :
    k += 1
    num = int(input("{}번째 도전! 원하시는 숫자를 입력하세요 >>".format(k)))
    inputlist.append(num)
    if num == a :
        print("축하합니다. 당첨입니다.")
        break
    elif num < a :
        print("입력하신 수는 랜덤숫자보다 작습니다. 더 큰 수를 입력하세요. ")
    elif num > a :
        print("입력하신 수는 랜덤숫자보다 큽니다. 더 작은 수를 입력하세요. ")
print("입력하신 숫자는",inputlist,"입니다.")
if k == 10 :
    print("랜덤숫자는",a,"였습니다.")