# a = [1,2,3,4,5]
# b = a # 얕은 복사
# c = [*a]    # 전개연산자
# a[1] = 20
# print(b)    # 데이터 값 변경
# print(c)    # 데이터 값 미변경

product = ['새우깡','90g',1200,3]

print("상품명 : {}, 무게 : {}, 가격 : {}원, 유통기한 : {}년".format(product[0],product[1],product[2],product[3]))
print("상품명 : {}, 무게 : {}, 가격 : {}원, 유통기한 : {}년".format(*product))  # 위와 동일하게 출력됨 ->변수 내에서 뽑아옴
