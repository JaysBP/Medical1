import pandas as pd
import numpy as np
pd.set_option("display.max_columns",None)
df = pd.DataFrame({
    '번호' : [1,2,3,4,5,6,7,8,9],
    '이름': ['홍길동','이순신','장영실','김유신','강감찬','김정호','유관순','안창호','윤봉길'],
    '국어점수' : [90,85,50,100,95,70,85,90,85],
    '영어점수' : [88,90,100,75,77,65,86,90,95],
    '수학점수' : [96,70,88,100,68,72,90,95,85],
})
    
# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t합격여부')
# print('-'*80)
# num = int(input("번호를 입력하세요 >>"))
# name = input("이름을 입력하세요 >>")
# kor = int(input("국어점수를 입력하세요 >>"))
# eng = int(input("영어점수를 입력하세요 >>"))
# math = int(input("수학점수를 입력하세요 >>"))
# tot = kor + eng + math
# avg = tot / 3
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(num,name,kor,eng,math,tot,avg,1))

# if avg > 80 :
#     print("{}님 합격입니다.".format(name))
# else :
#     print("{}님 불합격입니다.".format(name))