# split() - 문자열 분리
# hobby = "게임,골프,독서"
# print(hobby.split(","))     # 최초에 () 일때는 문자열 그대로 리스트에 들어가는 거고, ()안에를 나눠주면 개별로 리스트에 들어감.


# a_list = "2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"
# a_data = "2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"

# a_data = a_list.split("/")
# print(a_list)
# print(a_data)

# ss = "%"
# print(ss.join("파이썬"))

# s_date = "2023/03/08"
# s_date_list = s_date.split("/")

# s_time = "2023:03:08:16:48:00"
# s_time_list = s_time.split(":") 
# print(s_time_list)

# today = "2024/03/08"
# today_list = today.split("/")
# today_list[0] = '2034'
# print(today_list)

# today_list = ['2024','03','08']
# today_list[0] = int(today_list[0]) + 10
# print(today_list[0])
# t_list = list(map(int,today_list))
# print(t_list)

#  5개의 숫자를 입력하라

# list = []
# for i in range(5) :
#     list(map(int,input("숫자를 입력하세요 >>")))
# print(list)

# int_list = [10,20,30,40,50]
# str_list = list(map(str,int_list))
# print(str_list)