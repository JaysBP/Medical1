#  리스트 상 숫자들이 몇 번 나왔는지 딕셔너리로 출력하라
import operator

# numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
# counter = {}

# for n in numbers :
#     if n not in counter :
#         counter[n] = 0
#     counter[n] += 1
# print(counter)
# print(sorted(counter.items(),key=operator.itemgetter(0)))

array = ["F", "D", "A", "C", "A", "C", "F", "B", "C", "E", "C", "C", "F", "A", "B", "E", "F", "E"]
counter = {}

for i in array :
    if i not in counter :
        counter[i] = 0
    counter[i] += 1
print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0)))