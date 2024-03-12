# a = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
a = [[0]*5 for _ in range(5)]       # 컴프리헨션..?
value = 1
for i in range(0,5) :
    for j in range(0,5) :
        a[i][j] = value
        value += 1
print(a)