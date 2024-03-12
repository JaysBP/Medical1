
member = []
cnt = 0
while True :
    print('-'*80)
    print('1. 입력')
    print('2. 전체출력')
    print('3. 검색출력')
    print('4. 검색삭제')
    print('5. 수정')
    print('0. 종료')
    ch = int(input('원하는 번호를 입력하세요 >>'))
    print('-'*80)
    ch = int(ch)
    if ch == 1:
        print('[입력]')
        name = input('이름을 입력하세요 >>')
        cnt += 1
        m = [cnt, name]
        member.append(m)
        
    elif ch == 2:
        print('[전체출력]')
        print('번호 \t 이름')
        for i in range(len(member)):
            print('{} \t {}'.format(member[i][0],member[i][1]))
            
    elif ch == 3 :
        print('[검색출력]')
        m = 0
        name = input('검색하실 이름을 입력하세요 >>')
        for mem in member :
            # print(m)
            if name in mem :
                print('{}님은 존재합니다.'.format(name))
                m = 1
        if m == 0 :
            print('{}님은 존재하지 않습니다.'.format(name))

        # searname= input('검색하실 이름을 입력하세요)
        # print('번호\t이름)
        #     for i,m in enumerate(member) :
        #         if searname in m :
        #             print('{}\t{}'.format(member[i][0],member[i][1]))

    elif ch == 4 :
        print('[검색삭제]')
        nna = input("삭제할 이름을 입력하세요 >>")
        ck = 0
        for i, mem in enumerate(member) :
            if nna in mem :
                del(member[i])
                ck = 1
        if ck == 0 :
            print("{}님은 존재하지 않습니다.".format(nna))
            
    elif ch == 5 :
        print('[수정]')
        rename = input("수정할 사람의 이름을 입력하세요 >>")
        for i,m in enumerate(member) :
            if rename in m:
                print(rename,'님을 선택하셨습니다.')
                ch_num = input("수정할 항목을 선택하시오 (1.번호//2.이름) >>")
                if ch_num == '1' :
                    print(rename,'님의 번호 수정을 선택하셨습니다.')
                    print(rename,'님의 번호는',member[i][0],'입니다.')
                    newnum = input("수정할 번호를 입력해주세요 >>")
                    newnum = int(newnum)
                    member[i][0] = newnum
                elif ch_num == '2' :
                    print(rename,'님의 이름 수정을 선택하셨습니다.')
                    print(rename,'님의 이름은',member[i][1],'입니다.')
                    newname = input("수정할 이름를 입력해주세요 >>")
                    member[i][1] = newname
                else :
                    print('잘못입력하셨습니다.')
                    break
    elif ch == 0:
        print('[종료]')
        break
    else :
        print('다시 입력하세요.')