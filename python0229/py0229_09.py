student = []
cnt = 0
while True :
    print("-" * 80)
    print('\t[학생성적프로그램]')
    print('-' * 80)
    print('1.학생성적입력')
    print('2.학생성적수정')
    print('3.학생성적삭제')
    print('4.학생성적전체출력')
    print('5.학생검색출력')
    print('6.등수처리')
    print('0.프로그램종료')
    print('-'*35)
    choice = int(input('원하는 서비스의 번호를 입력하세요 >>'))
    if choice == 1 :
        print('1. 학생성적입력을 선택하셨습니다.')
        number = 0
        name = input('학생의 이름을 입력하세요 >>')
        kor = int(input('국어점수를 입력하세요 >>'))
        eng = int(input('영어점수를 입력하세요 >>'))
        math = int(input('수학점수를 입력하세요 >>'))
        tot = kor + eng + math
        avg = tot / 3
        cnt += 1
        stu = [number,name,kor,eng,math,tot,avg]
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(number,name,kor,eng,math,tot,avg))
        student.append(stu)
        print('성적입력이 완료되었습니다. 확인이 필요할 시 출력메뉴를 이용하여 주시길 바랍니다.')
    elif choice == 2 :
        print('2. 학생성적수정을 선택하셨습니다.')
    elif choice == 3 :
        print('3. 학생성적삭제를 선택하셨습니다.')
    elif choice == 4 :
        print('4. 학생성적전체출력을 선택하셨습니다.')
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        for i in range(len(student)) :
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[i][0],student[i][1],student[i][2],student[i][3],student[i][4],student[i][5],student[i][6]))
    elif choice == 5 :
        print('5. 학생성적검색출력을 선택하셨습니다.')
        search = 0
        searchName = input("검색하실 학생의 이름을 입력하세요 >>") 
        for sn in searchName :
            if name in sn :
                print("{}님의 정보입니다.".format(searchName))
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(number,name,kor,eng,math,tot,avg))
                # search = 1
        if search == 0 :
            print('{}님의 정보가 존재하지 않습니다.'.format(searchName))
    elif choice == 6 :
        print('6. 등수처리를 선택하셨습니다.')
    elif choice == 0 :
        print('프로그램을 종료합니다.')
        break
    else :
        print('없는 메뉴입니다. 다시 확인하시고 선택해주세요.')
        