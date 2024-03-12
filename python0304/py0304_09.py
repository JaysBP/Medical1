a = 10
b = a
b = 100

a_list = [1,2,3]
b_list = a_list     # 리스트는 같은 주소값을 공유하기에 이렇게 복사하면 애초에 같은 값으로 저장이 된다. 
b_list[0] = 200

print(a_list[0])
print(b_list[0])