# Define the axiom and the four rules
axiom = 'MI'

def rule1(s, n):
    if s.endswith("I"):
        return s + "U"
    else:
        return None

def rule2(s, n):
    if s.startswith("M"):
        return s + s[1:]
    else:
        return None

def rule3(s, n):
    if s[n:n+3] == "III":
        return s[:n] + "U" + s[n+3:]
    else:
        return None

def rule4(s, n):
    if s[n:n+2] == "UU":
        return s[:n] + "" + s[n+2:]
    else:
        return None


# Define a function to generate the proof tree for a formula
def proof_tree(formula):
    # Start with the axiom
    if formula == axiom:
        return {
            "formula": formula,
            "proof": [('axiom', axiom)],
            "depth": 0
        }

    # Apply each rule and recursively generate the proof tree
    for i in range(len(formula)):
        # Rule 1: If a string ends with I, add U at the end
        res = rule1(formula, i)
        if res is not None:
            proof1 = proof_tree(res)
            if proof1 is not None:
                return {
                    "formula": formula,
                    "proof": [('axiom', axiom), ('rule1', res)] + proof1["proof"],
                    "depth": proof1["depth"] + 1
                }

        # Rule 2: If a string begins with M, double everything after M
        res = rule2(formula, i)
        if res is not None:
            proof2 = proof_tree(res)
            if proof2 is not None:
                return {
                    "formula": formula,
                    "proof": [('axiom', axiom), ('rule2', res)] + proof2["proof"],
                    "depth": proof2["depth"] + 1
                }

        # Rule 3: If III occurs in a string at position n, replace it with U
        res = rule3(formula, i)
        if res is not None:
            proof3 = proof_tree(res)
            if proof3 is not None:
                return {
                    "formula": formula,
                    "proof": [('axiom', axiom), ('rule3', res)] + proof3["proof"],
                    "depth": proof3["depth"] + 1
                }

        # Rule 4: If UU occurs in a string at position n, delete it
        res = rule4(formula, i)
        if res is not None:
            proof4 = proof_tree(res)
            if proof4 is not None:
                return {
                    "formula": formula,
                    "proof": [('axiom', axiom), ('rule4', res)] + proof4["proof"],
                    "depth": proof4["depth"] + 1
                }

    # If none of the rules apply, return None
    return None


# Generate the proof tree for each formula
formulas = ['MI', 'MIU', 'MII', 'MUI', 'MU', 'MIIIU', 'MUIUI', 'MUIU']

proofs = {}
for i, formula in enumerate(formulas):
    proof = proof_tree(formula)
    if proof is not None:
        proofs[i] = proof

print(proofs)
