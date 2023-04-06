# def uppercase_all(strings):
#     result = []

#     for s in strings:
#         result.append(s.upper())


#     return result


def uppercase_all(strings):
    return [s.upper() for s in strings]




input = [
    "arrays in JavaScript, lists in Python",
    "objects in JavaScript, dictionaries in Python"
]

print(uppercase_all(input))
