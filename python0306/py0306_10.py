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
    search = input("성적 삭제를 위해 검색할 학생의 이름을 입력하세요(0. 취소) >>")
    check = 0
    if search == "0" :
        break
    for s_dic in students :
        if s_dic["name"] == search :
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