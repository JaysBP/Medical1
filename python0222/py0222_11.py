# 예제 5)
# 숫자를 입력받아 양수면 양수, 음수면 음수를 출력하라
num = -10
if num >= 0 :
    print("양수입니다.")
else :
    print("음수입니다.")

num = int(input("수를 입력하시오 >>"))
if num > 0 :
    print("입력하신 수는 양수입니다.")
elif num == 0:
    print("입력하신 수는 0입니다.")
else :
    print("입력하신 수는 음수입니다.")