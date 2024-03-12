
# 각각의 리스트에 프랑스, 프랑스어를 추가하라. // for문 사용해서 각각 출력하라
# con = ['미국','영국','일본','중국','스페인']
# lan = ['영어','영어','일본어','중국어','스페인어']

# con.append('프랑스')
# lan.append("프랑스어")
# # print(con, lan)

# for i in range(len(con)) :
#     print("{}은/는 {}를 사용합니다.".format(con[i],lan[i]))
    
# 입력 - 이름, 점수 => 총 3명의 정보를 member 리스트에 넣어라

# member = []

# for i in range(3):
#     na = input("이름을 입력하세요 >>")
#     sc = int(input("점수를 입력하세요 >>"))
#     member.append([na,sc])
# print(member)

# member = [['홍길동', 60], ['유관순', 55], ['이순신', 95]]
# # 60점 이상일 시에 OOO님 합격입니다. 미만이면 불합격입니다. 출력
# for m in range(len(member)) :
#     if member[m][1] >= 60 :
#         print("{}님 합격입니다.".format(member[m][0]))
#     else :
#         print("{}님 불합격입니다.".format(member[m][0]))

# 1 - 100까지의 합을 구하라
# n = 0
# for i in range(1,101,1) :
#     n += i
# print(n)

# 1 - 100까지 짝수들의 합을 구하라.
# n = 0
# for i in range(0,101,2) :
# #     n += i
# # print(n)
#     if n % 2 == 0 :
#         n += i
# print(n)
# # 1 - 100까지 홀수들의 합을 구하라.
# n = 0
# for i in range(1,100,2):
#     n += i
# print(n)

#  1 - 10 까지의 합
# num = [1,2,3,4,5,6,7,8,9,10]
# n = 0
# for i in range(1,11,1) :
#     n += i
# print(n)
# n = 0
# for i in num :
#     n += i
# print(n)


#  n1 - n2까지의 합을 구하라. 입력받아서
# n1 = int(input("첫번째 숫자를 입력하세요 >>"))
# n2 = int(input("두번째 숫자를 입력하세요 >>"))
# n1, n2 = n2,n1
# n = 0
# for i in range(n1,n2+1,1) :
#     n += i
# print(n)

# if n1 < n2 :
#     pass
# else :
#     n1,n2 = n2,n1
# print(n1,n2)

# odd_list = []

# for i in range(n1,n2+1) :
#     if i % 2 == 1 :
#         odd_list.append(i)
# print(odd_list)