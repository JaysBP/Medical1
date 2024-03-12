food = {'떡볶이' : '어묵', '짜장면' : '단무지', '라면' : '김치', '피자' : '피클', '맥주' : '땅콩', '삼겹살' : '상추'}

# 키의 값을 출력하시오
# value 값을 출력하시오
# key: value 의 형태로 출력하라
import operator

print(food.keys())
for key in food :
    print(key,end='\t')
print(food.values())
for key in food :
    print(food[key],end='\t')
print(sorted(food.items(), key = operator.itemgetter(0)))
for key in food :
    print(f"{key} : {food[key]}")