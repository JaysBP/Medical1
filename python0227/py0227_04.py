# 입력 : 이름, 아이디, 비밀번호
# 5명을 입력받아서 member list 작성
member = []

for i in range(3) :
    na = input("이름을 입력하세요 >>")
    id = input("아이디를 입력하세요 >>")
    pw = int(input("비밀번호를 입력하세요 >>"))
    m = [na,id,pw]
    member.append(m)
    print("\t이름\t아이디\t비밀번호\n")
    print("\t{}\t{}\t{}\n".format(na,id,pw))