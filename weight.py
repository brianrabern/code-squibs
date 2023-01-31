def order_weight(strng):

    dic={}
    for c in strng.split(' '):
        dic[c]=[]

    for i in dic:
        dic[i]=list(i)

    zdic={}
    for i in dic:
        zdic[i]=[]

    for k in dic:
        for i in k:
            zdic[k].append(int(i))

    for k,v in zdic.items():
        zdic[k] = sum(v)

    return zdic



    # d ={}

    # for k,v in sorted(zdic.items(), key=lambda i: i[1]):
    #     d[k] = v

    # final ={}
    # for v in d.values():
    #     if d[k]

    # return d



    # f = [x for x in d]
    # x=''
    # for item in f:
    #     x += item + ' '
    # return x


    # zdic={}
    # for i in dic:
    #     zdic[i]=[]

    # print(zdic)


    # for k in dic.values():
    #     print(sum(k))

    # return dic

    # zdic={}
    # for i in range(len(mlist)):
    #     zdic[i] = []
    #     for j in mlist[i]:
    #         zdic[i].append(int(j))
    # flist=[]
    # for y in zdic.values():
    #     flist.append(sum(y))

    # return sorted(flist)





# print(order_weight("56 65 74 100 99 68 86 180 90"))
# print(order_weight("103 123 4444 99 2000"))
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
