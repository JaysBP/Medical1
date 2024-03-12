student = []

for i in range(5) :
    print('-'*80)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력')
    print('4.학생성적전체출력')
    print('0.프로그램 종료')
    print('-'*80)
    ch = input('원하는 번호를 입력하세요 >>')
    # print(ch)
    if ch == '1' :
        print("[학생성적입력]")
        num = int(input("번호를 입력하세요 >>"))
        name = input("이름을 입력하세요 >>")
        kor = int(input("국어점수를 입력하세요 >>"))
        eng = int(input("영어점수를 입력하세요 >>"))
        math = int(input("수학점수를 입력하세요 >>"))
        tot = kor+eng+math
        avg = tot/3
        rank = num
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t석차")
        print('-' * 80)
        m = [1,name,kor,eng,math,tot,avg,rank]
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(num,name,kor,eng,math,tot,avg,rank))
        student.append(m)
        print(student)
        
    elif ch == '4' :
        print("[학생성적전체출력]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t석차")
        print('-' * 80)
        for m in range(len(student)) :
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                student[m][0],student[m][1],student[m][2],student[m][3],
                student[m][4],student[m][5],student[m][6],student[m][7]))

        
print('-' * 80)

print("프로그램이 종료되었습니다.")