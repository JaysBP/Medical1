# strip() - 공백제거
# ss = "    파이썬     "
# sss = "파이썬"
# print(ss.strip())      # 좌우측 공백 모두 제거.
# print(ss.lstrip())      # 좌측 공백만 제거하기 때문에 우측에 공백이 있으면 틀리게 나옴.
# print(ss.rstrip())      # 우측 공백만 제거하기 때문에 좌측에 공백이 있으면 틀리게 나옴.
# if ss.lstrip() == sss :
#     print('맞음')
# else :
#     print('틀림')
# sss = "파이썬"
# s_input = input("현재 배우고 있는 과목은 무엇인가요? >>").strip()
# if s_input == sss :
#     print("정답입니다.")
# else :
#     print("틀렸습니다.")

# replace - 문자열을 다른 문자열로 대체 -> print(a.replace("b","c")) : a에서 b를 c로 대체한다.

news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다. 2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. 지난해 이마트 창립 이후 적자를 기록했고, 신세계그룹 매출이 감소하는 등 사업 환경이 악화하면서 위기 극복을 위한 새로운 리더십을 내세웠다."
print(news.replace(" ",""))
print(news.replace("그룹",'group'))