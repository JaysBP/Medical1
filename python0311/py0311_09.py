# 매개변수 / 리턴값 모두 순서 맞춰주고 위아래 모두 똑같이 써주면 된다. 
# 리스트 형태라면 리턴을 쓰지 않아도 자리값을 찾아서 대입을 해주면 된다. 
# --------------------------------------------------------------------------------------------------------
# def stu_update(student) :       # 리스트 형태라서 주소값 자체가 저장되어 있다.
#     student[0] = 2
#     student[1] = '유관순'
#     student[5] = student[2] + student[3] + student[4]
#     student[6] = student[5] / 3
    

# # 프로그램 구현
# student = [1,'홍길동',100,100,100,0,0]

# # 함수호출
# stu_update(student)

# print("학생1 : ",student)

# --------------------------------------------------------------------------------------------------------
def stu_update(student) :       # 리스트 형태라서 주소값 자체가 저장되어 있다.
    student['stuNo'] = 2
    student["name"] = '유관순'
    student["total"] = student["kor"] + student["eng"] + student["math"]
    student["avg"] = student["total"] / 3
    
# 프로그램 구현
student = {'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 0, 'avg': 0}

# 함수호출
stu_update(student)

print("학생1 : ",student)
# --------------------------------------------------------------------------------------------------------

