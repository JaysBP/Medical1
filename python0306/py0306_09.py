students = [
            {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67},
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 98, 'eng': 98, 'math': 97, 'total': 293, 'avg': 97.67},
            {'stuNo': 'S004', 'name': '김구', 'kor': 97, 'eng': 97, 'math': 96, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 96, 'eng': 96, 'math': 95, 'total': 287, 'avg': 95.67}
]

# print("{} + {} = {}".format(students[3]["kor"],students[3]['eng'],students[3]["kor"] + students[3]['eng']))

# students[2]["kor"] = 100
# print(students)


# check = 0
# for s in students :
#     print(f"{check}.{s['name']}",end=' ')
#     check += 1

# 모든 학생의 국어점수를 출력하라 (0.OOO,00점)
check = 0
for s in students :
    print(f"{check}. {s['name']} : {s['kor']}점")
    check += 1
    
print('-' * 50)
for i,s in enumerate(students) :
    print(f"{i}. {s['name']} : {s['kor']}점")