# # 숫자 2개를 입력받고 연산자를 입력받아 무한히 계산하는 게산기를 만드는데 첫번째 숫자에 0을 입력하면 프로그램이 종료가 될 수 있게 하라.
# # n1 = int(input("첫번째 숫자를 입력하세요 >>"))
# # con = input("연산자를 입력하세요 >>")
# # n2 = int(input("두번째 숫자를 입력하세요 >>"))
# while True :
#     n1 = int(input("첫번째 숫자를 입력하세요 >>"))
#     if n1 == 0 :
#         print('종료되었습니다.')
#         break
#     con = input("연산자를 입력하세요 >>")
#     n2 = int(input("두번째 숫자를 입력하세요 >>"))
#     if con == '+' :
#         print("{} + {} = {}".format(n1,n2,n1+n2))
#     elif con == '-' :
#         print("{} + {} = {}".format(n1,n2,n1-n2))
#     elif con == '*' :
#         print("{} * {} = {}".format(n1,n2,n1*n2))
#     elif con == '/' :
#         print("{} / {} = {}".format(n1,n2,n1/n2))
#     else :
#         print("연산을 잘못 입력하셨습니다.")
