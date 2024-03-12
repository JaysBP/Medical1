# list = [
#     [0,0,0],[0,0,0],[0,0,0]
# ]

# a_lists = []
# for i in range(3) :
#     a_list = []
#     for j in range(3) :
#         a_list.append(3*i+j+1)
#     a_lists.append(a_list)
# print(a_lists)

# list = []
# for i in range(9) :
#     list.append(i+1)
# print(list)

# # 아래 식 풀이 - 0부터 8까지의 수를 n에다가 넣어서 n+1 하여 [리스트]에 담아라.
# list2 = [n+1 for n in range(9)]
# print(list2)


list3 = [[0]*3 for n in range(3)]
print(list3)

numList = [num*num for num in range(1,6)]
print(numList)