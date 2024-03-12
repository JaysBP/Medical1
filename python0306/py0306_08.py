students = [
            {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67},
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 98, 'eng': 98, 'math': 97, 'total': 293, 'avg': 97.67},
            {'stuNo': 'S004', 'name': '김구', 'kor': 97, 'eng': 97, 'math': 96, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 96, 'eng': 96, 'math': 95, 'total': 287, 'avg': 95.67}
]
subject = ['순번','학번','이름','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
count = len(students)+1   # 학번

while True :
    search = input("검색할 학생의 이름을 입력하세요(0. 취소) >>")
    check = 0
    if search == "0" :
        break
    for s_dic in students :
        if s_dic["name"] == search :
            break
        check += 1
        
    print("찾고자 하는 학생의 위치 : {}".format(check))

    if check == len(students) :     # 학생 수만큼 for문을 돌면
        print(f"{search} 학생의 데이터가 존재하지 않습니다. 다시 입력하세요.")
    else :
        print("{} 학생의 데이터가 존재합니다.".format(search))
        while True :
            s_input = int(input("수정하려는 과목을 선택하세요.(1.국어 // 2.영어 // 3. 수학 // 0/.취소) >>"))
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
            elif s_input == "0" :
                print("점수 수정을 취소합니다.")
                break        