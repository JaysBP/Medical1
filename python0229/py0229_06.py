# # for문으로 각각의 요소 추출
# num = [[10,20],[30,40],[50,60]]
# for i in range(len(num)) :
#     for j in range(len(num[i])) :
#         print(num[i][j],end=' ')
        
# i = 0
# while i < len(num) :
#     j = 0
#     while j < len(num[i]) :
#         print(num[i][j],end=' ')
#         j += 1
#     i += 1
   
   
# 예제 1) 이름을 검색해보고, 삭제
students = [[1,'홍길동',100],[2,'이순신', 90],[3,'유관순',85],[4,'김유신',70],[5,"김구",95]]
while True :
    print('1. 학생검색')
    print('2. 학생삭제')
    ch = input("원하는 번호를 입력해주세요 >>")
    if ch.isdigit() :
        ch = int(ch)
    if ch == 1: 
        na = input("검색할 학생의 이름을 입력하세요 >>")
        chk = 0
        for stu in students :
            # print(stu)
            if na in stu :
                print("{} 학생이 존재합니다.".format(na))
                print(stu)
                chk = 1
        if chk == 0:
            print('검색하신 학생이 존재하지 않습니다.')
    elif ch == 2 :
        nna = input("삭제할 학생의 이름을 입력하세요 >>")
        ck = 0
        for i, stu in enumerate(students):
            if nna in stu :
                del(students[i])
                ck = 1
                print(nna,'학생이 삭제되었습니다.')
        if ck == 0 :
            print(nna,'학생이 존재하지 않습니다.')
        # print(students)
    elif ch == 3 :
        print("프로그램이 종료되었습니다.") 
        break

    else :
        print("잘못입력했습니다. 다시 입력하세요.")
    
# str1 = '10'
# print(str1.isdigit())
# str2 = 'a'
# print(str2.isdigit())

  
# while True :
#     n = input("원하는 번호를 입력해주세요 >>")
#     if n.isdigit() :                            # 숫자지만 문자열일 때
#         n = int(n)
#     else :
#         print("문자가 입력되었습니다. 다시 입력하세요.")
#     if n == 0 :
#         print("숫자 0이 입력되었습니다.")