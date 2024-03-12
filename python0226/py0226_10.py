# numL = []

# # 0부터 5까지 넣어라
# print(numL)
# numL.append(0)
# numL.append(1)
# numL.append(2)
# numL.append(3)
# numL.append(4)
# numL.append(5)
# print(numL)

# # 방법 1)
# for i in range(0,6,1) :
#     numL = i
#     print(numL , end = ' ')
    
# # 방법 2)
# for i in range(6) :
#     num.append(i)

# aa = [1,2,3,4]

# for i in aa :
#     print(i)
    
# for i in range(0,4) :
#     print(aa[i])


# f = ['사과','복숭아','딸기','포도','자몽']

# for i in f :
#     print(i)
    
# for i in range(0,len(f)) :
#     print(f[i])                     # 리스트 길이 - len 함수는 반복문에서 사용됨.

# 각기 다른 국가 모두 출력하기 - 2가지 방법 모두

# c = ['미국','영국','호주','캐나다','일본','중국']

# for i in c :
#     print(i)
    
# for i in range(len(c)) :
#     print((c[i]))
    
# 1-100까지 들어가는 numL =[]를 만들고 출력해보기

# numL = []
# for i in range(1,101,1) :
#     numL.append(i)
    
# for i in range(100) :
#     numL.append(i+1)

# print(numL)

# # 반복문 내에 조건문 사용 - 조건문 상 충족하는 내용 외에는 그대로 출력
# for i in range(10) :
#     print(i)                # 0~9까지 출력
#     if i == 9 :
#         print('9입니다.')
        
# lan= ['영어','스페인어','일본어','중국어']
# for i in lan :
#     if i == '영어' :
#         print('영어입니다.')
#     else :
#         print('다른 언어입니다.')
        
# # 1-100 사이의 2의 배수만 출력  * if 조건문 사용 시 else에 의미가 없다면 사용하지 않아도 된다

# for i in range(2,101,2) :
#     print(i,end=' ')
    
# for i in range(0,100) :
#     if i % 2 == 0 :
#         print(i+2,end=" ")

# # # 1-100 사이의 7의 배수만 출력
# for i in range(7,101,7) :
#     print(i,end=' ')
    
# for i in range(100) :
#     if (i+1) % 7 == 0 :
#         print(i+1, end=' ')

# # 80점 이상만 출력 - 합격이 5번 출력
# aa = [100,90,86,79,72,52,98,94]

# for i in aa :
#     if i >= 80 :
#         print('합격입니다.')


# # 딸기가 있으면 딸기, 다른 과일은 다른 과일이라고 출력

# f = ['사과','복숭아','딸기','포도','자몽']

# for i in f:
#     if i == '딸기' :
#         print("딸기입니다.")
#     else :
#         print('다른 과일입니다.')
        
# # 홀수는 홀수, 짝수는 짝수로 출력

# num = [1,2,5,7,9,10,23,43]

# for i in num :
#     if i % 2 == 0:
#         print("짝수",end='')
#     else :
#         print("홀수",end='')

# for i in range(len(num)) :
#     # print(i)                          # 각 요소의 번호를 뜻함 -> i = 0,1,2,3,4
#     print(num[i])                       # num 자체의 요소를 보여줌 -> i = num[0],num[1],num[2]
#     if num[i]%2 == 0:
#         print('짝수')
#     else :
#         print("홀수")