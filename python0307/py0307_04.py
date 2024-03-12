# 명사 단어 10개, 동사 10개, 형용사 10개
words = [
    {"airplane" : "비행기","apple" : "사과","bakery" : "빵집","banana" : "바나나","bank" : "은행","bean" : "콩","bicycle" : "자전거","boat" : "보트","bowl" : "그릇","bus" : "버스"},
    {"run" : "달리다","walk" : "걷다","sit" : "앉다","stand" : "서다","sleep" : "자다","read" : "읽다","look" : "보다","do" : "하다","feel" : "느끼다","go" : "가다"},
    {"accumulated":"누적된","additional":"추가적인","adequate":"적당한","administrative":"관리의","affordable":"알맞은","alternative":"대체 가능한","annual":"해마다의","different":"다른","local":"지역의","social":"사회의"}
]

w_title = ["","명사","동사","형용사"]

while True :
    print("[ 영단어 맞추기 프로그램 ]")
    print("-" * 60)
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print("0. 종료")
    print("-" * 60)
    choice = int(input("원하는 번호를 입력하세요 >>"))

    if choice == 1 :
        wrong = []
        count = 0
        print(f"{w_title[choice]}를 선택하셨습니다.")
        check = input("퀴즈를 시작하시겠습니까?(1.시작 0.취소) >>")
        if check == "1" :
            # print(w_noun.keys())        # 전체 key값 출력
            # print(w_noun.values())      # 전체 value값 출력
            for key in words[choice] :
                # print(key,":",w_noun[key])                # 전체 key값 출력
                answer = input(f"{key}의 뜻은 무엇일까요? >>")
                if answer == words[choice][key] :
                    print("정답입니다.")
                    count += 1
                else :
                    print(f"오답입니다. 정답은 {words[choice][key]}입니다.")
                    wrong.append(words[choice][key])
            print(f"퀴즈가 종료되었습니다. 10문제 중 {count}문제를 맞췄고, {len(wrong)}문제를 틀렸습니다.")
            print(f"틀린 단어는 {wrong}입니다.")
        else :
            print("퀴즈를 취소하셨습니다.")
            break


    elif choice == 2 :
        wrong = []
        count = 0
        print(f"{w_title[choice]}를 선택하셨습니다.")
        check = input("퀴즈를 시작하시겠습니까?(1.시작 0.취소) >>")
        if check == "1" :
            # print(w_noun.keys())        # 전체 key값 출력
            # print(w_noun.values())      # 전체 value값 출력
            for key in words[choice] :
                # print(key,":",w_noun[key])                # 전체 key값 출력
                answer = input(f"{key}의 뜻은 무엇일까요? >>")
                if answer == words[choice][key] :
                    print("정답입니다.")
                    count += 1
                else :
                    print(f"오답입니다. 정답은 {words[choice][key]}입니다.")
                    wrong.append(words[choice][key])
            print(f"퀴즈가 종료되었습니다. 10문제 중 {count}문제를 맞췄고, {len(wrong)}문제를 틀렸습니다.")
            print(f"틀린 단어는 {wrong}입니다.")
        else :
            print("퀴즈를 취소하셨습니다.")
            break
        
    elif choice == 3 :
        wrong = []
        count = 0
        print(f"{w_title[choice]}를 선택하셨습니다.")
        check = input("퀴즈를 시작하시겠습니까?(1.시작 0.취소) >>")
        if check == "1" :
            # print(w_noun.keys())        # 전체 key값 출력
            # print(w_noun.values())      # 전체 value값 출력
            for key in words[choice] :
                # print(key,":",w_noun[key])                # 전체 key값 출력
                answer = input(f"{key}의 뜻은 무엇일까요? >>")
                if answer == words[choice][key] :
                    print("정답입니다.")
                    count += 1
                else :
                    print(f"오답입니다. 정답은 {words[choice][key]}입니다.")
                    wrong.append(words[choice][key])
            print(f"퀴즈가 종료되었습니다. 10문제 중 {count}문제를 맞췄고, {len(wrong)}문제를 틀렸습니다.")
            print(f"틀린 단어는 {wrong}입니다.")
        else :
            print("퀴즈를 취소하셨습니다.")
            break
        
    elif choice == 0 :
        print("프로그램을 종료합니다.")
        break