import random

fruits = {'peach' : '복숭아','orange' : '오렌지','apple' : '사과' ,
         'pear' : '배','grape' : '포도','mango' : '망고','kiwi' : '키위'}

# print(fruits['peach'])
# 키값을 넣어서 value값을 얻어내는 방법

# f_list = ['peach','pear','kiwi']
# print(fruits[f_list[0]])            # 복숭아 출력
# for f in f_list :
#     print(fruits[f])

# 딕셔너리에서 찾을 때는 키값을 우선적으로 알아야 한다.

f_list = list(fruits.keys())
print(f_list)
f_list_ran = random.sample(f_list,4)
print("랜덤추출 :",end=' ')
for f in f_list_ran :
    print(fruits[f],end=' ')   


# print(len(fruits))
# # 랜덤으로 4개 출력 - 랜덤은 리스트만 가능 -> key를 리스트 타입으로 변경해야 한다. 
# # print(random.sample(4))           # 잘못된 방법

# print(fruits.keys())                #딕셔너리에서 key값 추출
# print(random.sample(list(fruits.keys()),4))

# # 4개의 랜덤 key를 출력하라

# f_list = random.sample(list(fruits.keys()),4)
# f_list2 = ["kiwi", "grape", "peach","pear"]

# print(fruits[f_list2[0]])

