students = [[1,'홍길동',100,100,99,299,99.97,1],
            [2,'유관순',100,100,99,299,99.97,1],
            [3,'이순신',100,100,99,299,99.97,1],
            [4,'김구',100,100,90,290,96.67,1],
            [5,'김유신',90,70,50,210,70.00,1],
            [6,'강감찬',100,100,100,300,100.0,1]
]

# 등수처리 - 성적처리 내에선 합계를 통해 비교
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