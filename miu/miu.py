
# pylint: disable-all


def axiom():
    '''axiom: MI'''
    return ['M', 'I']


def rule1(s):
    '''Rule 1: xI → xIU'''
    t = s[:]
    if t[-1] == 'I':
        t.append('U')
    return t


def rule2(t):
    '''Rule 2: Mx → Mxx'''
    t = s[:]
    if t[0] == 'M':
        d = t[1:]
    return t+d


def rule3(t, n):
    '''Rule 3: xIIIy → xUy'''
    t = s[:]
    I_list = []

    for index in range(len(t)-2):
        if t[index] == 'I' and t[index+1] == 'I' and t[index+2] == 'I':
            I_list.append([index, index+1, index+2])
    if I_list:
        pos = I_list[n][0]
        g = t[0:pos] + ['U'] + t[pos+3:]
        return g


def rule4(t, n):
    '''Rule 4: xUUy → xy'''
    t = s[:]
    U_list = []

    for index in range(len(t)-1):
        if t[index] == 'U' and t[index+1] == 'U':
            U_list.append([index, index+1])
    if U_list:
        pos = U_list[n][0]
        g = t[0:pos] + t[pos+2:]
        return g


################

def generate():

    theorems = {0: {"formula": 'MI',
                    "proof": [('axiom','MI')],
                    "depth": 0}}

    for i in range(4):

        theorem = theorems[i].copy()

        if theorem["formula"] != rule1(theorem["formula"]):
            theorems[i+1] = {}
            theorems[i+1]["formula"] = rule1(theorem["formula"])

            theorems[i+1]["proof"] = [theorem["formula"]] + \
                [rule1(theorems[i]["formula"])]
            theorems[i+1]["path"] = theorem["path"]+['Rule 1']

            theorems[i+1]["depth"] = theorem["depth"] + 1

    return theorems


print(generate())


# theorems = {0: {"formula": ['M', 'I'], "proof": [
#     ['M', 'I']], "path": ['Axiom'], "depth": 0}}

# theorem = theorems[0].copy()
# print(theorem)

# print(theorem["formula"] != rule1(theorem["formula"]))

# print(theorems[0])
# theorems[1] = {}
# print(theorems)

# theorems[1]["formula"] = rule1(theorem["formula"])

# print(theorems)
# theorems[1]["proof"] = theorem["proof"].append(rule1(theorems[0]["formula"]))
# theorems[1]["path"] = theorem["path"].append('Rule 1')
# theorems[1]["depth"] = theorem["depth"] + 1

# print(theorems)

# print(theorems[0]["formula"] == rule1(theorems[0]["formula"]))
# print(theorems[0]["formula"])
# print(rule1(theorems[0]["formula"]))
# print(theorems[0]["depth"])
# num = theorems[0]["depth"] + 1
# print(num)


# theorem = {"formula": ['M', 'I', 'I', 'U'],
#            "proof": [], "rules": [], "depth": 0}

# print(theorem)

# print("rule1(rule4(rule3(rule3(rule2(rule2(rule2(axiom()))), 5), 2), 0)):")
# #

# print(axiom())
# print(rule2(axiom()))
# print(rule2(rule2(axiom())))
# print(rule2(rule2(rule2(axiom()))))
# print(rule3(rule2(rule2(rule2(axiom()))), 5))
# print(rule3(rule3(rule2(rule2(rule2(axiom()))), 5), 2))
# print(rule4(rule3(rule3(rule2(rule2(rule2(axiom()))), 5), 2), 0))
# print(rule1(rule4(rule3(rule3(rule2(rule2(rule2(axiom()))), 5), 2), 0)))
