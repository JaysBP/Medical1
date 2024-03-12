students = [
            {'stuNo': 'S001', 'name': '홍길동', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67},
            {'stuNo': 'S002', 'name': '유관순', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 96, 'eng': 96, 'math': 95, 'total': 287, 'avg': 95.67},
            {'stuNo': 'S004', 'name': '김구', 'kor': 97, 'eng': 97, 'math': 96, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 98, 'math': 97, 'total': 293, 'avg': 97.67}
]

# 등수처리 - 합계를 활용하여 처리해야 한다.
for i,s in enumerate(students) :
    rank_count = 1 # 등수 처리 변수 설정
    for j in students :
        if s['total'] < j['total'] :    # 두 수를 비교하여
            rank_count += 1             # 현재 학생의 합계보다 크면 1 증가 // 
    s['rank'] = rank_count

print(students)