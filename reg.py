
def find_outer_parenthesis(s):
    counter = 0
    start = -1
    end = -1
    for i, c in enumerate(s):
        if c == "(":
            if counter == 0:
                start = i
            counter += 1
        elif c == ")":
            counter -= 1
            if counter == 0:
                end = i
    return [start, end]


print(find_outer_parenthesis("((()))"))


def parse_calculation(s):
    operator = s[0]
    args = s[1:].split()
    print(args)
    return eval(args[0] + operator + args[1])


print(parse_calculation("- 10 15"))
