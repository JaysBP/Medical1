n1 = int(input("첫번째 수를 입력하세요 >>"))
cal =input("수식을 입력하세요 >>")
n2 = int(input("두번째 수를 입력하세요 >>"))

if cal == "+" :
    print("{}".format(n1+n2))
elif cal == "-" :
    print("{}".format(n1-n2))
elif cal == "*" :
    print("{}".format(n1*n2))
elif cal == "/" :
    print("{}".format(n1/n2))
else :
    print("오류입니다. 다시 입력해주세요.")
