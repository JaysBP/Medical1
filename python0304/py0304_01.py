students = []   # 학생 성적 사용
students = [[1,'홍길동',100,100,99,299,99.97,1],
            [2,'유관순',100,100,99,299,99.97,1],
            [3,'이순신',100,100,99,299,99.97,1],
            [4,'김구',100,100,90,290,96.67,1],
            [5,'강감찬',100,100,100,300,100.0,1]
]
cnt = len(students) # 학번 사용
while True :
    print('-' * 80)
    print("[학생성적프로그램]")
    print('-' * 80)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생성적검색')
    print('4. 학생성적수정')
    print('5. 등수처리')
    print('6. 학생성적삭제')
    print('0. 프로그램 종료')
    print('-' * 80)
    choice = input('원하는 번호를 입력하세요 >>')
    if not choice.isdigit() :
        print('숫자만 입력 가능합니다.')
        continue    # 현재 반복문 다시 실행
    choice = int(choice)

    
    # 1번. 학생성적입력 프로그램 시작부분
    if choice == 1 :
        while True :        # 무한반복
            print("학생성적을 입력합니다.")
            print('-' * 80)
            student = []
            name = input('이름을 입력하세요( 0 : 취소 ) >>')
            if name == '0' :
                break
            cnt += 1        # 학번 추가
            student.append(cnt)
            student.append(name)
            student.append(int(input("국어점수를 입력하세요 >>")))
            student.append(int(input("영어점수를 입력하세요 >>")))
            student.append(int(input("수학점수를 입력하세요 >>")))
            sum = student[2]+student[3]+student[4]
            # 합계 저장
            student.append(sum)
            # 평균 저장
            student.append("{:.2f}".format(sum/3))
            students.append(student)
            # 전체 학생 출력
            print(students)
        
    # 2번. 학생성적 전체출력 프로그램 시작부분
    elif choice == 2 :
        pass
        print('전체 학생의 성적을 출력합니다.')
        print('-' * 50)
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-" * 50)

        # 전체출력
        for stu in students :
            for s in stu :
                print(s,end="\t")
            print()
        print('-' * 50)

    # 3번. 학생성적검색 프로그램 시작부분
    elif choice == 3 :
        print('검색하신 학생의 성적을 출력합니다.')        
        while True :
            search = input("검색하고 싶은 학생을 입력하세요 >>")
            check = 0   # 찾는 정보 확인용
            count = 0
            if search =="0" :
                break
            for stu in students :
                if search in stu :
                    check = 1
                    break
                count += 1
                
            if (check == 1) :
                print("{}님의 학생정보는 존재합니다.".format(search))
                # 전체학생 정보출력
                print('{} 학생의 성적을 출력합니다.'.format(search))
                print('-' * 50)
                print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
                print("-" * 50) 
                for i in students[count] :
                    print(i,end="\t")
                print()
            else :
                print("학생정보가 존재하지 않습니다.")   
    # 4번. 학생성적수정 프로그램 시작부분
    elif choice == 4 :
        print('검색하신 학생의 성적을 수정합니다.') 
        while True :
            search = input("찾는 학생의 이름을 입력하세요 (취소 : 0)>>")
            if search == "0" :
                break
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
        # 영어점수 변경 후 합계,평균 또한 수정되어야 한다.
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
        # 수핟점수 변경 후 합계,평균 또한 수정되어야 한다.
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                    students[count][6] = float("{:.2f}".format(students[count][5] / 3))
        # 출력
                    print(students)
                else :
                    print("성적수정처리가 진행되지 않았습니다.")

    # 5번. 등수처리 프로그램 시작부분
    elif choice == 5 :
        print("등수처리 프로그램입니다.")
        while True :
            choice= input("등수처리를 실행하시겠습니까? (0:취소//1:실행) >> ")
            if choice == "0" :
                print("등수처리를 취소하셨습니다.")
                break
            else :
                # 등수처리 진행
                for i_stu in (students) :
                    no = 1          # 등수 초기화
                    for j_stu in (students) :
                        # 각각의 총합을 비교하는 식
                        if i_stu[5] < j_stu[5] :
                            no += 1
                            # 등수 위치에 등수 no 투입
                    i_stu[7] = no
            print("등수처리가 완료되었습니다.")
            print('-' * 50)
            print("[ 등수확인 ]")
            print(students)

    # 6번. 학생정보삭제 프로그램 시작부분
    elif choice == 6 :
        print("학생정보삭제 프로그램입니다.")
        while True :
            search = input("삭제하려는 학생의 이름을 입력하세요 >>")
            # 이름찾기
            count = 0
            for i, stu in enumerate(students) :
                if stu[1] == search :
                    break
                count += 1
            if count == len(students) :
                    print("검색하신 {} 학생이 존재하지 않습니다.".format(search))
            else :
                    choice = int(input("검색하신 {} 학생이 존재합니다. 삭제하시겠습니까? (1. 삭제)>>".format(search)))
                    if choice == 1 :
                        print('{} 학생의 데이터가 삭제되었습니다.'.format(search))
                        del students[count]
                    else :
                        print('삭제요청이 취소되었습니다.')

            print(students) 
            print('-' * 50)
        
    # elif choice == 0 :
    #     print('프로그램을 종료합니다.')
    #     break   # 반복문 종료