import random

# 4조740
# 만약 내가 2조 711 이라고 넣으면 7 하나만 맞은 거임.
# 앞자리는 1 - 9까지 가능
first_num = random.randint(1,9)
last_num = random.randint(0,999999)
# 뒷자리는 0 - 999999까지 가능
lotto = str(first_num)+"조"+"{:06d}".format(last_num)
# print(lotto)

print(lotto)
lotto = "1조740042"
lotto_num = str(input("주택복권 번호를 입력하세요 [ex) O조OOO]>>"))
count = 0
# for i in range(len(lotto)) :
#     if lotto[:5] != lotto_num[:5] :
#         if lotto[6] == lotto_num[6] :
#             print("1만원 당첨입니다.")
#             count += 1
#     elif lotto[:4] != lotto_num[:4] :
#         if lotto[5:] == lotto_num[5:] :
#             print("10만원 당첨입니다.")
#             count += 1

# print(f"맞은 갯수는 {count-1}개 입니다.")
a = "1조123456"
b = "9조123456"
for i in range(len(a),0,-1) :
    if i == 2 : continue
    if a[i-1] != b[i-1] :
        break
    else :
        count += 1      # 맞은 횟수 1 증가
        
if count == 0 :
    print("꽝입니다.")
elif count == 1 :
    print("마지막 자리가 맞았습니다. 당첨금액은 1만원입니다.")
elif count == 2 :
    print("5,6번째 자리가 맞았습니다. 당첨금액은 0만원입니다.")
elif count == 3 :
    print("4,5,6번째 자리가 맞았습니다. 당첨금액은 100만원입니다.")
elif count == 4 :
    print("3,4,5,6번째 자리가 맞았습니다. 당첨금액은 1000만원입니다.")
elif count == 5 :
    print("2,3,4,5,6번째 자리가 맞았습니다. 당첨금액은 1억원입니다.")
elif count == 6 :
    print("6번째 자리까지 모두 맞았습니다. 당첨금액은 10억원입니다.")