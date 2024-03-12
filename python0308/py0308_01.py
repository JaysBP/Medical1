#  1 - 10까지 입력하세요
list = []
# 풀이 1) 기본 for문 사용
for i in range(0,10) :
    list.append(i+1)
print(list)

# 풀이 2) comprehension
list = [i for i in range(1,11)]
print(list)

# 풀이 3) 공간 먼저 만들고 값을 넣는 방법
list = [0] * 10
for i in range(10):
    list[i] = i+1
print(list)