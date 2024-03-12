#  1 - 100까지 더하는데 총합이 100이 넘었을 때의 수를 출력하라.
i = 1
s = 0

while i <= 100 :
    s += 1
    if s > 100:
        break
    i += 1


sum = 0
for i in range(1,101) :
    sum += i
    print(sum)
    if sum > 100 :
        break
print("수 :",i)
print("총합 :",sum)