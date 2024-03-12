import operator

# 딕셔너리 정렬
t_dic = {}
t_list = []
t_dic = {'peach' : '복숭아','orange' : '오렌지','apple' : '사과' ,'pear' : '배','grape' : '포도','mango' : '망고','kiwi' : '키위'}

# print(t_dic.keys()) # 키값
# print(t_dic.values())   # 밸류값
# print(t_dic.items())    #튜플

t_list = sorted(t_dic.items(),key = operator.itemgetter(0),reverse=False)
print(t_list)





# a = [5,7,4,8,1,9,3,2]
# a.sort()
# print(a)

# b = [5,7,4,8,1,9,3,2]
# b.sort(reverse=True)
# print(b)

# 3개의 수를 입력받아 순서대로 출력하라 17,50,12
# a = []
# for i in range(0,3) :
#     num = int(input('원하시는 숫자를 입력하세요 >>'))
#     a.append(num)
#     a.sort()
# print(max(*a))