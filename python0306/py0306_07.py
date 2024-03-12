students = [
            {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67},
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 98, 'eng': 98, 'math': 97, 'total': 293, 'avg': 97.67},
            {'stuNo': 'S004', 'name': '김구', 'kor': 97, 'eng': 97, 'math': 96, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '강감찬', 'kor': 96, 'eng': 96, 'math': 95, 'total': 287, 'avg': 95.67}
]
count = len(students)+1   # 학번
# for s in students :
#     print(s)
while True :
    count = input("학생 전체 성적을 출력하시겠습니까? (1.출력 2.취소)")
    if count == 0 :
        break
    print("[ 학생성적전체출력 ]")
    print('-' * 55)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
    print('-' * 55)
    for s_dic in students :
        for s_key in s_dic :
            print(s_dic[s_key],end='\t')
        print()
    print('-' * 55)
    


#     name = input("수정할 학생의 이름을 입력하세요 >>")
#     if name in students :
#         print("{} 학생은 존재합니다. 수정하시겠습니까?(0:수정, 1:취소)".format(name))
#     else:
#         print("{} 학생은 존재하지 않습니다.".format(name))
#         break