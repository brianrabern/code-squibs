# dictionary = {
#     "dog": 1,
#     "number": "three",
#     "size": "2",
#     "heavy": True,
#     "weight": 3.4,
# }
# total = sum_summables(dictionary)
# print(total) # --> 7.4

# print(isinstance(1, int))       # --> True
# print(isinstance("cat", str))   # --> True
# print(isinstance(True, int))    # --> True, what?! Did you know this?
# print(isinstance("cat", int))   # --> False
# print(isinstance(1, str))       # --> False

def sum_summables(dictionary):
    total = 0

    for key in dictionary:
        if isinstance(dictionary[key], int) or isinstance(dictionary[key], float):
            total += dictionary[key]
        elif isinstance(dictionary[key], str) and dictionary[key].isnumeric():
                total += float(dictionary[key])
    return total



dictionary = {
    "dog": 1,
    "number": "three",
    "size": "2",
    "heavy": True,
    "weight": 3.4,
}
print(sum_summables(dictionary))

# print(True.isnumeric())
print(isinstance(True, int))


isinstance(True, int) == True
isinstance(True, bool) == True
