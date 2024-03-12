stu1 = [1,'홍길동',100,100,100,300,100.0,1]
stu2 = [2,'유관순',90,90,90,270,90.0,2]
stu3 = [3,'이순신',80,80,80,240,80.0,3]

print('-'*80)
print('[학생성적프로그램]')
print('-'*80)
print('1. 학생성적입력')
print('2. 학생성적수정')
print('3. 학생성적삭제')
print('4. 학생성적전체출력')
print('5. 학생성적검색출력')
print('6. 등수처리')
print('0. 프로그램 종료')
print('-'*80)

choice = int(input("원하는 번호를 입력하시오 >>"))
print('-' * 80)
if choice == 1 :
    print("1. 학생성적입력을 선택하셨습니다.")
    num = int(input("번호를 입력하세요 >>"))
    name = input("이름을 입력하세요 >>")
    kor = int(input("국어점수를 입력하세요 >>"))
    eng = int(input("영어점수를 입력하세요 >>"))
    math = int(input("수학점수를 입력하세요 >>"))
    tot = kor + eng + math
    avg = tot / 3
    rank = num
    print('-'*80)
    print("{} {} {} {} {} {} {} {}".format('번호','이름','국어','영어','수학','합계','평균','등수'))    
    print("{} {} {} {} {} {} {:.2f} {}".format(num,name,kor,eng,math,tot,avg,rank))
    print("성적입력이 완료되었습니다.")  
elif choice == 4 :
    print("4.학생성적전체출력을 선택하였습니다.")
    print('-' * 80)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}"
          .format(stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7],
                  stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7],
                  stu3[0],stu3[1],stu3[2],stu3[3],stu3[4],stu3[5],stu3[6],stu3[7]))