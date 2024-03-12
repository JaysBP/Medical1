# 예제 5 - 원의 넓이를 출력하라

pi = 3.141592
r = input("반지름 값을 입력하시오 >>")
r = int(r)

print("원의 넓이: {:.3f}".format(pi*(r**2)))
print("원의 둘레: {:.3f}".format(2*pi*r))