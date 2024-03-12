# students = [[S001,'홍길동',100,100,99,299,99.97,1],
#             [S002,'유관순',100,100,99,299,99.97,1],
#             [S003,'이순신',100,100,99,299,99.97,1],
#             [S004,'김구',100,100,90,290,96.67,1],
#             [S005,'강감찬',100,100,100,300,100.0,1]
# ]

students = [
            {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67},
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 98, 'eng': 98, 'math': 97, 'total': 293, 'avg': 97.67},
            {'stuNo': 'S004', 'name': '김구', 'kor': 97, 'eng': 97, 'math': 96, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 96, 'eng': 96, 'math': 95, 'total': 287, 'avg': 95.67}
]
count = len(students)+1   # 학번
while True :
    name = input("{}번째 학생의 이름을 입력하세요 (0:취소)>>".format(len(students)+1))
    if (name=="0") :
        print("학생성적 입력을 취소합니다")
        break
    student = {}    # 데이터 초기화    
    student["stuNo"] = "S"+"{:03d}".format(count)
    student["name"] = name  # 딕셔너리 추가
    kor = int(input("국어점수를 입력하세요 >>"))
    student["kor"] = kor
    eng = int(input("영어점수를 입력하세요 >>"))
    student["eng"] = eng
    math = int(input("수학점수를 입력하세요 >>"))
    student["math"] = math
    total = kor + eng + math
    student["total"] = total
    avg = total / 3
    student['avg'] = float("{:.2f}".format(avg))
    # 리스트에 추가
    students.append(student)
    count += 1
    print("입력 데이터 :{}".format(student))    # list -> dict
    print(students)