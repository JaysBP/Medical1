# 예제 1)
# stu = ['홍길동','유관순','이순신','김구','강감찬']
# # 1. 이순신 출력 // 2. 김구 -> 안창호로 변경 // 3. 유관순부터 강감찬 출력 // 4. 왕건 추가, 홍길동 삭제
# print("1번 :",stu[2])

# stu[3] = '안창호'
# print("2번 :", stu)

# print("3번 :",stu[1:])

# # stu.append('왕건')
# # stu.remove("홍길동")
# # print("4,5번 :", stu)

# stu.append("왕건")
# del(stu[0])
# print("4,5번 :", stu)

# 예제 2)
# f = ['사과', '복숭아', "딸기", '배', '포도', "수박"]
# 1. 딸기출력//2.포도->망고//3.복숭아,딸기출력//4.사과추가//5.감추가//6.사과삭제//7.수박있다고 출력
# print('1번 :',f[2])

# f[4] = '망고'
# print('2번 :',f)

# print('3번 :', f[1:3])

# f.append('사과')
# f.append('감')
# print("4,5번 :", f)

# del(f[0])
# print("6번 :", f)

# f.remove('사과')
# print("6번 :", f)

# if '수박' in f :
#     print("7번 : 수박이 있습니다.")
# else :
#     print("7번 : 수박이 없습니다.")

# 예제 3)
# num = [10,20,30,40,50]
# 1. 60이 없으면 60 추가 // 2. 20있으면 70추가 20 삭제

# if 60 not in num :
#     num.append(60)
# else :
#     print(num)

# print(num)

# if 20 in num :
#     num.append(70) 
#     num.remove(20)
# else :
#     print(num)
    
# print(num)

# 리스트 형태의 리스트 내에서 특정 값 추출

# aa = [[1,2],[3,4]]
# print(aa[0][1])

# 예제 4) 

# 1. 유관순 출력 // 2. 홍길동 80점으로 수정 // 3. 이순신 95점을 student에 추가

# stu1 = ['홍길동',90]
# stu2 = ['유관순',100]
# student = [stu1, stu2]

# print("1번 :",student[1][0])

# student[0][1] = 80
# print("2번 :",student)

# stu3 = ['이순신', 95]
# student.append(['이순신', 95])
# student = [stu1,stu2,stu3]
# print("3번 :", student)

# if student[1][1] == 100 :
#     print("4번 : 100점입니다.")
# else :
#     print("4번 : 100점이 아닙니다.")