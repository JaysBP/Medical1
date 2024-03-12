fruit = {'peach' : '복숭아','orange' : '오렌지','apple' : '사과' ,
         'pear' : '배','grape' : '포도','mango' : '망고','kiwi' : '키위'}

# 복숭아 영어로 입력하시오
case = []
case_w = []
for f in fruit :
    eng_in = input("{}를 영어로 입력하세요 >>".format(fruit[f]))
    if eng_in == f :
        print('정답입니다.')
        case.append(f)
    else :
        print('오답입니다. 정답은 {}입니다.'.format(f))
        case_w.append(f)
    
print("총 {}개 맞추셨습니다 오답은 {}개이며 {}를 틀렸습니다.".format(len(case),len(case_w),case_w))
    
    
    
    # print("입력하신 단어는 {}입니다.".format(eng_in))