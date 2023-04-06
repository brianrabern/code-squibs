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


# If UU occurs in a string at position n, delete it
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


# Define a function to generate all theorems and their proof paths up to a certain length

def generate_theorems(max_length):
    # Start with the axiom and its proof path
    theorems = {axiom: [axiom]}
    # Set to keep track of the theorems already processed
    processed = set([axiom])
    # Queue of theorems to be processed
    queue = [(axiom, 0)]
    # While the queue is not empty and the maximum length is not reached
    while queue:
        # Get the next theorem and its proof path
        theorem, path = queue.pop(0)
        # If the theorem has reached the maximum length, skip it
        if len(theorem) > max_length:
            continue
        # Apply all rules to the theorem and get new theorems
        new_theorems = apply_rules(theorem)
        # For each new theorem
        for new_theorem in new_theorems:
            # If it has not been processed yet
            if new_theorem not in processed:
                # Add it to the theorems and its proof path
                theorems[new_theorem] = theorems[theorem] + [new_theorem]
                # Add it to the processed set
                processed.add(new_theorem)
                # Add it to the queue to be processed
                queue.append((new_theorem, len(theorems[new_theorem])-1))
                print(theorems)
    return theorems


print(generate_theorems(10))
