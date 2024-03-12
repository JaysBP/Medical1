student = [0,"홍길동",0,0,0,0,0,0]

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
        num1 = int(input("번호를 입력하세요 >>"))
        name1 = input("이름을 입력하세요 >>")
        kor1 = int(input("국어점수를 입력하세요 >>"))
        eng1 = int(input("영어점수를 입력하세요 >>"))
        math1 = int(input("수학점수를 입력하세요 >>"))
        tot = kor1+eng1+math1
        avg = tot/3
        rank = num1
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t석차")
        print('-' * 80)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(num1,name1,kor1,eng1,math1,tot,avg,rank))
        a = ("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(num1,name1,kor1,eng1,math1,tot,avg,rank))
        num2 = int(input("번호를 입력하세요 >>"))
        name2 = input("이름을 입력하세요 >>")
        kor2 = int(input("국어점수를 입력하세요 >>"))
        eng2 = int(input("영어점수를 입력하세요 >>"))
        math2 = int(input("수학점수를 입력하세요 >>"))
        tot = kor2+eng2+math2
        avg = tot/3
        rank = num2
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t석차")
        print('-' * 80)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(num2,name2,kor2,eng2,math2,tot,avg,rank))
        b = ("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(num2,name2,kor2,eng2,math2,tot,avg,rank))
        student = [a,b]
    elif ch == '4' :
        print("[학생성적전체출력]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t석차")
        print('-' * 80)
        for i in range(len(student)) :
            print(student)
            
    elif ch == '0' :
        print("[프로그램 종료]")
    else :
        print("잘못 입력하셨습니다.")
        
print('-' * 80)

print("프로그램이 종료되었습니다.")