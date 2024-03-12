# 국어, 영어, 수학 점수를 입력받아 평균을 출력하라. 
# 출력 - 평균은 95점입니다. 

kor = input("국어점수를 입력하시오 >>")
kor = int(kor)
eng = input("영어점수를 입력하시오 >>")
eng = int(eng)
math = input("수학점수를 입력하시오 >>")
math = int(math)
avg = (kor+eng+math)/3

print("{} {} {}" .format("평균은", avg,"점입니다."))  # NO.1
print("평균은 : {}점 입니다.".format(avg))            # NO.2