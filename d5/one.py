# d1 = {"a":1, "b":2}
# d2 = {"b":"bbb", "c": "ccc"}
# d3 = merge_dictionaries(d1, d2)
# print(d3) # --> {"a":1, "b":"bbb", "c": "ccc"})
# Hint: dict.copy() will make a copy of a dictionary

def merge_dictionaries(d1, d2):

    d3 = d1

    for key,value in d2.items():
        d3[key] = value

    return d3


d1 = {"a":1, "b":2}
d2 = {"b":"bbb", "c": "ccc"}

print(merge_dictionaries(d1, d2))
