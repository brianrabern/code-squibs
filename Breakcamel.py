def solution(s):

    mlist =[]
    for i in s:
        if i.islower():
            mlist.append(i)
        else:
            mlist.append(' ')
            mlist.append(i)

    return ''.join(mlist)




print(solution("breakCamelCase"))
