aa = [[1,2,[3,4]],[5,6],[7,8,9]]
aaa = [[[1,2],[3,4,5]],[[6],[7,8,9]]]
for i in aa :
    for j in i :
        if isinstance(j,list) :
            for k in j:
                print(k)
        else :
            print(k,end=' ')
# a = [1,2,3,4,5]
# for i in a :
#     print(i,end=' ')