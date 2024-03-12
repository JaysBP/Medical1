import operator

fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {}            # 딕셔너리 생성

for f in fruit :
    if f not in counter :   # 딕셔너리에 키가 존재하는지 확인
        counter[f] = 0  # 딕셔너리에 키가 없을 때 키값을 추가        
    counter[f] += 1      # 키의 value값을 1 증가시킴

# print(counter)

# 딕셔너리 정렬 - key값을 기준으로 정렬
print(sorted(counter.items(),key=operator.itemgetter(0)))               # key값 기준 순차정렬
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))  # key값 기준 역순정렬
print(sorted(counter.items(),key=operator.itemgetter(1)))               # value값 기준 순차정렬
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))  # value값 기준 역순정렬
