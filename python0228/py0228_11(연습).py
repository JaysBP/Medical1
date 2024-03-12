#  1. 변수 선언
score =[
    [80,90,85], [70,80,90],[84,92,80],[72,81,76]
]
name = ['홍길동','유관순','이순신','김구']

total = []

#  2. 코딩
#  2-1. 요소 하나하나 출력하시오
# for i in range(len(score)):
#     for j in range(len(score[i])):
#         print(score[i][j],end=' ')
#  2-2. 작은 요소의 합을 구해서 total 리스트에 넣으시오 -> total = [255,240,256,229]
s = 0
for i in range(len(score)) :
    s = 0
    # print(score[i],end=' ')
    for j in range(len(score[i])) :
        s = s + score[i][j]
    total.append(s)
print(total)
#  3. 출력
#  3-1. 250점 미만 불합격 // 이상 합격
# print(total)
# print(name)
for i in range(4) :
    if total[i] >= 250 :
        print("{}님 합격입니다.".format(name[i]))
    else :
        print("{}님 불합격입니다.".format(name[i]))