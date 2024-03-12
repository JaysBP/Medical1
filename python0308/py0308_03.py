'''
[
    [0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0] 총 52개 만들어서 출력하라
]

'''
#  1차원 먼저 만들기
# list = [0] * 52
# print(list)
list = [0 for i in range(52)]
# 2차원 만들어주기(comprehension을 사용해야 얕은 복사를 방지할 수 있다. )
list = [[0]*2 for i in range(52)]
print(list)