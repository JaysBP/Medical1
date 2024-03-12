students = [[1,'홍길동',100,100,99,299,99.97,1],
            [2,'유관순',100,100,99,299,99.97,1],
            [3,'이순신',100,100,99,299,99.97,1],
            [4,'김구',100,100,90,290,96.67,1],
            [5,'강감찬',100,100,100,300,100.0,1]
]

while True :
    search = input("삭제하려는 학생의 이름을 입력하세요 >>")
    # 이름찾기
    count = 0
    for i, stu in enumerate(students) :
        if stu[1] == search :
            break
        count += 1
    if count == 5 :
            print("검색하신 {} 학생이 존재하지 않습니다.".format(search))
    else :
            print("검색하신 {} 학생이 존재합니다.".format(search))

    print("찾은 위치 : ", count)
    del students[count]
    print(students) 
    print('-' * 50)