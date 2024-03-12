students = [[1,'홍길동',100,100,99,299,99.97],
            [2,'유관순',100,100,99,299,99.97],
            [3,'이순신',100,100,99,299,99.97]
]


# 찾고자 하는 학생 찾기(전부 확인해서 없는 것도 나오는 ver.)
# while True :
#     search = input("검색하고 싶은 학생을 입력하세요 >>")
#     if search =="0" :
#         break
#     for stu in students :
#         if search in stu :
#             print("{}님의 학생정보를 찾았습니다.".format(search))
#             break
#         else :
#             print("{}님의 학생정보는 존재하지 않습니다.".format(search))
            

# 찾고자 하는 학생 찾기(상위 문제 업그레이드 ver.)
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
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-" * 50) 
        for i in students[count] :
            print(i,end="\t")
        print()
    else :
        print("학생정보가 존재하지 않습니다.")    