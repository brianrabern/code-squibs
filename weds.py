def shorter_than(strings,max_length):

    return [string for string in strings if len(string) <max_length]




input = [
    "base",
    "basket",
    "foot",
    "hand",
    "racquet",
    "we"
]

print(shorter_than(input,3))
