#  관계 연산자 - 두 변수(or상수) 간 차이를 비교//True,False로 표시
#  조건문, 반복문에 자주 사용됨.
#  a==b -> a와 b가 같다 // a!=b -> a와 b는 같지 않다.
# num = 95
# print(num==90)
# print(num>=90)
# print(num<=90)
# print(num!=90)

# 논리연산자
# and(둘 다 참이어야만 한다. )
# or(둘 중에 하나만 참이어도 가능)
# nor(두 입장이 같으면 참)
# ex)홍길동 100 100 100 유관순 90 100 90

# print("-"*35)
# print('\t[학생성적프로그램]')
# print('-'*35)
# print('1.학생성적입력')
# print('2.학생성적수정')
# print('3.학생성적삭제')
# print('4.학생성적전체출력')
# print('5.학생검색출력')
# print('6.등수처리')
# print('0.프로그램종료')
# print('-'*35)
# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
# num = input("번호를 입력하시오 >>")
# name = input("이름을 입력하시오 >>")
# kor = int(input('국어점수를 기입하시오 >>'))
# eng = int(input('영어점수를 기입하시오 >>'))
# math = int(input('수학점수를 기입하시오 >>'))
# tot = kor + eng + math
# avg = tot/3
# print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(1,'홍길동',100,100,100,300,100.0,1))
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(2,"유관순",90,100,90,int(kor+eng+math),int(kor+eng+math)/3,2))
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(num,name,kor,eng,math,tot,avg,4))