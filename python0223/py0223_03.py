id = "admin"
pwd = "1111"

uid = input("아이디를 입력하세요 >>")
upw = input("비밀번호를 입력하세요 >>")

# if id == uid :
#     if pwd == upw :
#         print("로그인이 완료되었습니다.")
#     else :
#         print("아이디 또는 비밀번호가 일치하지 않습니다.")
# else :
#     print("로그인이 정상적으로 이뤄지지 않았습니다..")
    
    
# 입력한 아이디가 같으면 비밀번호가 일치하는 비교해서 같으면 로그인되었습니다. 아니면 비밀번호 오류
# 아이디가 다르면 아이디가 일치하지 않습니다. 

if id == uid :
    if pwd == upw :
        print("로그인이 완료되었습니다.")
    else :
        print("비밀번호가 틀렸습니다.")
else :
    print("등록되지 않은 계정입니다.")