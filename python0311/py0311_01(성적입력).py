students = [
            {'stuNo': 'S001', 'name': '홍길동', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67},
            {'stuNo': 'S002', 'name': '유관순', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 96, 'eng': 96, 'math': 95, 'total': 287, 'avg': 95.67},
            {'stuNo': 'S004', 'name': '김구', 'kor': 97, 'eng': 97, 'math': 96, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 98, 'math': 97, 'total': 293, 'avg': 97.67}
]
count = len(students) + 1 
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
    choice = int(choice)

    

    if choice == 1 :
        while True :
            name = input("{}번째 학생의 이름을 입력하세요 (0:취소)>>".format(len(students)+1))
            if (name=="0") :
                print("학생성적 입력을 취소합니다")
                break
            student = {}       
            student["stuNo"] = "S"+"{:03d}".format(count)
            student["name"] = name  
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
           
            students.append(student)
            count += 1
            print("입력 데이터 :{}".format(student))          

    elif choice == 2 :
        while True :
            count = int(input("학생 전체 성적을 출력하시겠습니까? (1.출력 0.취소)"))
            if count == 0 :
                break
            print("[ 학생성적전체출력 ]")
            print('-' * 55)
            print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
            print('-' * 55)
            for dic in students :
                for key in dic :
                    print(dic[key],end='\t')
                print()
            print('-' * 55)

    elif choice == 3 :
        print('검색하신 학생의 성적을 출력합니다.')        
        while True :
            search = input("검색하고 싶은 학생을 입력하세요 >>")
            check = 0  
            count = 0
            if search == "0" :
                break
            for stu in students :
                if search in stu :
                    check = 1
                    break
                count += 1
                
            if check == 1 :
                print(f"{search}님의 학생정보는 존재합니다.")
                print(f"{search}학생의 성적을 출력합니다.")
                print('-' * 50)
                print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
                print("-" * 50) 
                for i in students :
                    print(i,end="\t")
                print()
            else :
                print("학생정보가 존재하지 않습니다.")   

    elif choice == 4 :
        s_title = ['','국어','영어','수학']
        print('검색하신 학생의 성적을 수정합니다.') 
        while True :
            search = input("검색할 학생의 이름을 입력하세요(0. 취소) >>")
            check = 0
            if search == "0" :
                break
            for dic in students :
                if dic["name"] == search :
                    break
                check += 1
                
            print("찾고자 하는 학생의 위치 : {}".format(check))

            if check == len(students) :   
                print(f"{search} 학생의 데이터가 존재하지 않습니다. 다시 입력하세요.")
            else :
                print("{} 학생의 데이터가 존재합니다.".format(search))
                while True :
                    s_input = int(input("수정할 과목을 선택하세요.(1.국어 // 2.영어 // 3. 수학 // 0/.취소) >>"))
                    if s_input == 1 :
                        s_1 = "kor"
                        print(f"[{s_title[s_input]}점수를 수정합니다.]")
                        print(f"{students[check]['name']} 학생의 {s_title[s_input]}점수는 {students[check][s_1]}점입니다.")
                        print('-' * 80)
                        score = int(input("수정할 점수를 입력하세요 >>"))
                        students[check][s_1] = score
                        students[check]['total'] = students[check][s_1] + students[check]['eng'] + students[check]['math']
                        students[check]['avg'] = float("{:.2f}".format(students[check]['total'] / 3))
                        print(f"{students[check]['name']} 학생의 {s_title[s_input]}점수가 {students[check][s_1]}점으로 수정되었습니다.")
                        print(students[check])
                    elif s_input == 2 :
                        s_1 = "eng"
                        print(f"[{s_title[s_input]}점수를 수정합니다.]")
                        print(f"{students[check]['name']} 학생의 {s_title[s_input]}점수는 {students[check][s_1]}점입니다.")
                        print('-' * 80)
                        score = int(input("수정할 점수를 입력하세요 >>"))
                        students[check][s_1] = score
                        students[check]['total'] = students[check]['kor'] + students[check][s_1] + students[check]['math']
                        students[check]['avg'] = float("{:.2f}".format(students[check]['total'] / 3))
                        print(f"{students[check]['name']} 학생의 {s_title[s_input]}점수가 {students[check][s_1]}점으로 수정되었습니다.")
                        print(students[check])
                    elif s_input == 3 :
                        s_1 = "math"
                        print(f"[{s_title[s_input]}점수를 수정합니다.]")
                        print(f"{students[check]['name']} 학생의 {s_title[s_input]}점수는 {students[check][s_1]}점입니다.")
                        print('-' * 80)
                        score = int(input("수정할 점수를 입력하세요 >>"))
                        students[check][s_1] = score
                        students[check]['total'] = students[check]['kor'] + students[check]['eng'] + students[check][s_1]
                        students[check]['avg'] = float("{:.2f}".format(students[check]['total'] / 3))
                        print(f"{students[check]['name']} 학생의 {s_title[s_input]}점수가 {students[check][s_1]}점으로 수정되었습니다.")
                        print(students[check])
                    elif s_input == 0 :
                        print("점수 수정을 취소합니다.")
                        break      

    elif choice == 5 :
        print("등수처리 프로그램입니다.")
        for i,s in enumerate(students) :
            rank_count = 1 
            for j in students :
                if s['total'] < j['total'] :    
                    rank_count += 1           
            s['rank'] = rank_count
        print("등수처리가 완료되었습니다.")
        print(students)

    elif choice == 6 :
        print("학생정보삭제 프로그램입니다.")
        while True :
            search = input("성적 삭제를 위해 검색할 학생의 이름을 입력하세요(0. 취소) >>")
            check = 0
            if search == "0" :
                break
            for dic in students :
                if dic["name"] == search :
                    break
                check += 1
                
            print("찾고자 하는 학생의 위치 : {}".format(check))
            
            if check >= len(students) :
                print("찾고자 하는 학생이 없습니다.")
            else :
                print(f"{search} 학생을 찾았습니다.")
                s_input = input(f"{search} 학생의 성적을 삭제하시겠습니까? (0. 취소) >>")
                if s_input != "1" :
                    print("삭제를 취소합니다.")
                    break
                else :
                    del students [check]
                    print(students)
                    print(f"{search} 학생의 성적이 삭제되었습니다.")
        
    elif choice == 0 :
        print('프로그램을 종료합니다.')
        break   
                    