ss = "파이썬 공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다."
print(ss.count("자바"))
print(ss.count("공부"))
print(ss.find("공부",7))      # 존재하는 문자열의 위치값 출력(뒤에 붙이는 값은 시작위치-> 뒤에 붙인 값의 자리부터 시작해서 뒤에 언제 나오는지 자리수 출력)
print(ss.find("자바"))      # 존재하는 문자열의 위치값 출력 - 없으면 -1 출력
print(ss.rfind("공부"))      # 반대에서 시작해서 몇번째 자리에 있는지 확인
print("-" * 70)
print(ss.index('공부'))
# print(ss.index('자바'))     # 존재하는 문자열의 위치값 출력 - 없으면 에러
print(ss.index('파이썬'))
print("-" * 70)
print(ss.startswith("파이썬"))  # 첫번째 문장부터 시작되는지 확인 - 맞으면 True 아니면 False
print(ss.endswith("않습니다.")) # 끝문장부터 시작확인
print("-" * 70)