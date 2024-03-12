# student = [[1,'홍길동',100,100,100,300,100.0,1],[2,'유관순',90,90,90,270,1]]
# print('-'*80)
# print('\t[학생성적프로그램]')
# print('1. 학생성적입력')
# print('4. 학생성적전체출력')
# print('-'*80)
# ch = int(input('원하는 번호를 선택하세요 >>'))
# if ch == 1 :
#     print("1. 학생성적입력을 선택하셨습니다.")
#     no1 = int(input("번호를 입력하세요 >>"))
#     na1 = input("이름을 입력하세요 >>")
#     ko1 = int(input("국어점수를 입력하세요 >>"))
#     en1 = int(input("영어점수를 입력하세요 >>"))
#     ma1 = int(input("수학점수를 입력하세요 >>"))
#     tot = ko1+en1+ma1
#     avg = tot/3
#     ra1 = no1
#     print("[{},{},{},{},{},{},{},{}]".format(no1,na1,ko1,en1,ma1,tot,avg,ra1))
#     stu1 = ("[{},{},{},{},{},{},{},{}]".format(no1,na1,ko1,en1,ma1,tot,avg,ra1))
#     student.append([stu1])
#     print(student)
# elif ch == 4 :
#     print("4. 학생성적전체출력을 선택하셨습니다.")
#     print("[학생성적전체출력]")
#     print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
#     print("[{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}]".format(
#         student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5],student[0][6],student[0][7]))
#     print("[{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}]".format(
#         student[1][0],student[1][1],student[1][2],student[1][3],student[1][4],student[1][5],student[1][6],student[1][7]))
# else :
#     print("추후 제작 예정")
