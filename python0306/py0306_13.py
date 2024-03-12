students = [
            {'stuNo': 'S001', 'name': '홍길동', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67},
            {'stuNo': 'S002', 'name': '유관순', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 96, 'eng': 96, 'math': 95, 'total': 287, 'avg': 95.67},
            {'stuNo': 'S004', 'name': '김구', 'kor': 97, 'eng': 97, 'math': 96, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 98, 'math': 97, 'total': 293, 'avg': 97.67}
]
student = {}
# 학생성적 입력부분 구현
count = 0
while True :
    print("[ 1. 학생성적입력 ]")
    print("[ 2. 학생성적전체출력 ]")
    print("[ 0. 프로그램 종료 ]")
    choice = int(input("사용할 메뉴의 번호를 입력하세요. >>"))
    if choice == 1 :
        print("[ 1. 학생성적입력 ] 메뉴입니다.")
        student['stuNo'] = 'S'+ "{:03d}".format(count)            
        student['name'] = input("학생의 이름을 입력하세요 >>")
        student['kor'] = int(input("국어성적을 입력하세요 >>"))
        student['eng'] = int(input("영어성적을 입력하세요 >>"))
        student['math'] = int(input("수학성적을 입력하세요 >>"))
        student['total'] = student['kor'] + student['eng'] + student['math']
        student['avg'] = float("{:.2f}".format(student['total']/3))
        students.append(student)
        print('-' * 80)
        print(student)
        print("성적입력이 완료되었습니다.")
        