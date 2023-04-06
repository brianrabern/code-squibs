

# Define the axiom of the MIU system
axiom = 'MI'


# Define the four rules of the MIU system

# If a string ends with I, add U at the end
def rule1(s, n):
    if s.endswith("I"):
        return s + "U"
    else:
        return None


# If a string begins with M, double everything after M
def rule2(s, n):
    if s.startswith("M"):
        return s + s[1:]
    else:
        return None


# If III occurs in a string at position n, replace it with U
def rule3(s, n):
    if s[n:n+3] == "III":
        return s[:n] + "U" + s[n+3:]
    else:
        return None


# If UU occurs in a string at poistion n delete it
def rule4(s, n):
    if s[n:n+2] == "UU":
        return s[:n] + "" + s[n+2:]
    else:
        return None


# Define a function to apply all rules to a given string and return new strings
def apply_rules(s):
    new_strings = set()
    for n, rule in enumerate([rule1, rule2, rule3, rule4]):
        for i in range(len(s)):
            result = rule(s, i)
            if result is not None:
                new_strings.add(result)
    return new_strings
