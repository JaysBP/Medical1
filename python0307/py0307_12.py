list = [1,2,3]
alist = list

list[0] = 100

print(alist)

# 얕은 복사 방지 - 깊은 복사
list = [1,2,3]
alist = [*list] # 방법 1
alist = list[:] # 방법 2
list[0] = 100
print(alist)