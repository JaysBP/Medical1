# list 형태 활용 - 대괄호로 감싸서 형태를 온전히 구축
# num = [1,2,3,4,5]
# # print(num)

# list1 = [1,2,3,4,5]
# list2 = ["사과","복숭아","딸기","자두","포도"]
# list3 = [1,'배','혈액형',99.1]
# python은 리스트 내에 여러 형태가 저장 가능 -> print(list3)

# print(list2)
# print(list2[1])
# print(list1[3])
# print(list3[3])

# print(list1[-1]) <- 뒤에서 부터 체킹

# print(len(list3))

# 예제 1) 리스트 내 딸기 추출
# print(list2[2])
# print(list2[2:3])
# print(list2[-3])

# # 슬라이싱 - 리스트 내 일정 부분 추출
# a = [0,1,2,3,4,5,6,7,8,9]
# print(a[1:4])
# print(a[3:8])
# print(a[5:])
# print(a[:5])

# 리스트 요소 확인 - 내부에 포함되어 있는지 여부 확인 방법
# print('포도' in list2)      # 원하는 요소 작성 후 in 변수 작성으로 변수에 포함된 리스트 중 존재여부 확인
# print('10' in list2)
# print(2 not in list1)

# lista = [1,2,3,["a","b","c"],[4,5]]
# print(lista[3])
# print([4,5] in lista)

