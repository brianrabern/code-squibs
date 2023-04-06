# def count_letters(string):
#     pass



def find_ha(string):
    h = []
    a = []
    for i, c in enumerate(string):
        if c == "H":
            h.append(i)
        if c == "A":
            a.append(i)
    for i in range(len(max(h, a))):
        count = 0
        if max(h) < min(a):
            count += 1
            h[:-1]
            a.pop(0)
    return count

# def find_h_a(string):
#     counter = 0
#     h = -1
#     a = -1
#     for i, c in enumerate(string):
#         if c == "H":
#             if counter == 0:
#                 h = i
#             counter += 1
#         elif c == "A":
#             counter -= 1
#             if counter == 0:
#                 a = i
#     return [h, a]


print(find_ha("HHHHHAAAAA"))
