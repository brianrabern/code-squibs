def find_nb(m):

    x=0
    n=0

    while (x < m):
        n+=1
        x += n**3
    if x == m:
        return n
    else: return -1





    # def to_inf():
    #     i = 0
    #     while True:
    #         yield i
    #         i += 1

    # x =0

    # for n in to_inf():
    #     n+=1
    #     x += n**3
    #     if x == m:
    #         return n
    #     else: return -1

        # if m == x:
        #     return n
        #     break
        # if n == round(m**(1/3)):
        #     return -1
        #     break
        # else:
        #     n += 1
        #     x += k**3







    # def to_inf():
    #     i = 0
    #     while True:
    #         yield i
    #         i += 1

    # x =0
    # n = -1

    # for k in to_inf():
    #     if m == x:
    #         return n
    #         break
    #     if n == round(m**(1/3)):
    #         return -1
    #         break
    #     else:
    #         n += 1
    #         x += k**3




print(find_nb(1))
print(find_nb(2))
print(find_nb(9))
print(find_nb(36))
print(find_nb(100))
print(find_nb(1071225))
print(find_nb(26825883955641))
print(find_nb(135440716410000))
print(find_nb(91716553919377))
print(find_nb(4183059834009))
# print(find_nb(917165539193778484848483720202023850569))
