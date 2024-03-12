
fruits = ['딸기','사과','자몽','포도','수박','자몽']

# 자몽을 삭제 - remove는 앞에 있는 게 삭제, del은 위치를 지정해서 삭제가 가능

for i, f in enumerate(fruits) :
    print("{}는 {}번째에 있습니다.".format(f,i))
    
for index, elem in enumerate(fruits) :
    print('{}는 {}번째에 있습니다.'.format(elem, index))