# 매개변수 / 리턴값 모두 순서 맞춰주고 위아래 모두 똑같이 써주면 된다. 

def stu_update(stuNo,name,kor,eng,math) :
    stuNo = 2
    name = '유관순'
    kor = 90
    total = kor+eng+math
    avg = "{:.2f}".format(total/3)
    return stuNo, name, kor, total, avg

# 프로그램 구현
stuNo = 1
name = "홍길동"
kor = 100
eng = 100
math = 100
total = 0
avg = 0

# 함수호출
stuNo, name, kor, total, avg = stu_update(stuNo,name,kor,eng,math)

print("학생1 : ",stuNo,name,kor,eng,math,total,avg)