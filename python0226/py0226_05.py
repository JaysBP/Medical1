#  얕은 복사, 깊은 복사 - 변수의 값이 변하게 되면 변하는 변수는 다른 메모리 주소로 옮겨진다.
# a = 1
# b = 2
# c = a
# print('변수:',a,b,c)
# a = 8
# print('변수:',a,b,c)

# print(id(a))
# print(id(b))
# print(id(c))
# print('변수:',a,b,c)

# list 형태의 경우, 여러 데이터가 들어갈 수 있기에 주소 값이 할당된다. -> 같은 위치값 변경, 다 바뀜

# 얕은 복사
# 단순 복사는 주소값이 복사가 된다.
# 단순 복사가 되었기에 aa값을 변경하면 cc의 값도 변경됨. list 형태일 때에 한정
# aa = [1]
# bb = [2]
# cc = aa

# print(aa,bb,cc)
# print(id(aa))
# print(id(bb))
# print(id(cc))

# aa[0] = 10

# print(aa,bb,cc)
# print(id(aa))
# print(id(bb))
# print(id(cc))

#  깊은 복사 - copy
# import copy
# aa = [1]
# bb = [2]
# cc = copy.deepcopy(aa)

# print(aa,bb,cc)
# print(id(aa))
# print(id(bb))
# print(id(cc))

# aa[0] = 10

# print(aa,bb,cc)
# print(id(aa))
# print(id(bb))
# print(id(cc))