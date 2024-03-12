# 이름, 국어, 영어, 수학을 입력받아 합계를 출력하라
students = []

for i in range(0,2) :
    student = [] # 초기화 시켜줘야 계속 겹치거나 축적되지 않음
    student.append(input('이름을 입력하세요 >>'))
    student.append(int(input("국어점수를 입력하세요 >>")))
    student.append(int(input("영어점수를 입력하세요 >>")))
    student.append(int(input("수학점수를 입력하세요 >>")))
    sum= student[1]+student[2]+student[3]
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))
    students.append(student)
    print(students)


print('[학생성적 출력]')    # 전체출력
print('-' * 50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-" * 50)

# 전체출력
for stu in students :
    for s in stu :
        print(s,end="\t")
    print()
print('-' * 50)

# 총 학생의 총국어 점수, 총영어점수, 총수학점수, 총합계, 총평균
korea = 0
english = 0 
maths = 0
total = 0
average = 0
#  [[],[],[]] 형태로 존재하는 리스트에서 일정 위치 지정하여 총합을 구함.
for i,stu in enumerate(students) :
    korea += stu[1]
    english += stu[2]
    maths += stu[3]
    total += stu[4]
average = total/len(students)
print('\t')    
print("",korea,english,maths,total,average,sep='\t')

# for stu in students :
#     for s in stu :
#         print(s,end="\t")
#     print()
# print('-' * 50)
# print("국어점수 총합 : ",'{}'.format(students[0][1]+students[1][1]+students[2][1]))