students = [[1,'홍길동',100,100,99,299,99.97],
            [2,'유관순',100,100,99,299,99.97],
            [3,'이순신',100,100,99,299,99.97]
]

while True :
    search = input("찾는 학생의 이름을 입력하세요 >>")
    check = 0
    count = 0
    for stu in students :
        if search in stu :
            check = 1
            break
        count += 1      # 검색한 이름의 위치를 찾기 위한 값
    if check == 0 :
        print("찾는 학생의 정보가 없습니다.")
    else :
        print("입력하신 {} 학생의 정보를 찾았습니다.".format(search))
        num = int(input("변경하실 과목을 골라주세요 >> 1. 국어  2. 영어  3. 수학  0. 취소>> "))
        if num == 1 :
            print("국어과목의 점수변경을 선택하셨습니다.")
# 성적 수정 프로그램 구현
            print("현재 {} 학생의 국어점수는 {}점입니다.".format(search, students[count][2]))
            num = int(input("변경하실 점수를 입력하세요 >>"))
            students[count][2] = num
            print("국어점수 변경처리가 완료되었습니다.")
# 국어점수 변경 후 합계,평균 또한 수정되어야 한다.
            students[count][5] = students[count][2]+students[count][3]+students[count][4]
            students[count][6] = float("{:.2f}".format(students[count][5] / 3))                    # 현재 문자처럼 되어 있기에 합계가 불가. 만약 바꾸려면 합계하거나 연산할 때 주의
# 출력
            print(students)
        elif num == 2 :
            print("영어과목의 점수변경을 선택하셨습니다.")
# 성적 수정 프로그램 구현
            print("현재 {} 학생의 영어점수는 {}점입니다.".format(search, students[count][3]))
            num = int(input("변경하실 점수를 입력하세요 >>"))
            students[count][3] = num
            print("영어점수 변경처리가 완료되었습니다..")
# 국어점수 변경 후 합계,평균 또한 수정되어야 한다.
            students[count][5] = students[count][2]+students[count][3]+students[count][4]
            students[count][6] = float("{:.2f}".format(students[count][5] / 3))
# 출력
            print(students)
        elif num == 3 :
            print("수학과목의 점수변경을 선택하셨습니다.")
# 성적 수정 프로그램 구현
            print("현재 {} 학생의 수학점수는 {}점입니다.".format(search, students[count][4]))
            num = int(input("변경하실 점수를 입력하세요 >>"))
            students[count][4] = num
            print("수학점수 변경처리가 완료되었습니다..")
# 국어점수 변경 후 합계,평균 또한 수정되어야 한다.
            students[count][5] = students[count][2]+students[count][3]+students[count][4]
            students[count][6] = float("{:.2f}".format(students[count][5] / 3))
# 출력
            print(students)
        else :
            print("성적수정처리가 진행되지 않았습니다.")
    elif num == 0 :
        print("종료되었습니다.")
        break