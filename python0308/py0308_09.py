import random
random_num = str(random.randint(10000,99999))
print("[랜덤숫자 맞추기]")
print(f"랜덤숫자 :", random_num)

count = 0
a_input = input('다섯자리 숫자를 입력하세요 >>')
# 숫자자리로 확인해서 맞춘 개수를 출력하시오
for i in range(len(str(random_num))) :
    if random_num[i] == a_input :
        count += 1
print(count)