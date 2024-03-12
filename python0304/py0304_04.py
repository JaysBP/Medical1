students = [['홍길동',100,100,99,299,99,97],['유관순',100,100,99,299,99,97],['이순신',100,100,99,299,99,97]]
kors = 0

# students는 2차원 배열 // stu는 1차원 배열이라서 오류가 났음
for i,stu in enumerate(students) :
    kors += stu[1]
print(kors)