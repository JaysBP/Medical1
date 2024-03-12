students = {"stuNo" : 1, "stuName" : "홍길동", "tel" : "010-0000-0000",
            "gender" : "male", "id" : "aaa", "pw" : 1111}

students['stuNo'] += 1

print(students["stuNo"])
# 키값이 없는 데이터를 불러오려 한다면 error이 뜬다. - 변수명 확인 잘해야 한다. 변수명 + key값까지
print(students["studentNo"])

if "studentNo" in students :
    print("key가 있습니다.")
    students["studentNo"] += 1
    print(students["studentNo"])
else :
    print("키가 존재하지 않습ㄴ디ㅏ.")