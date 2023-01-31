def reverse_entries(dictionary):
    new_dict = {}
    for key,value in dictionary.items():
        new_dict[value] = key
    return new_dict

def reverse_entries2(dictionary):
    return {value: key  for key,value in dictionary.items()}


a = {
    "hair": "red",
    "eyes": "blue",
}
print(a)

b = reverse_entries2(a)
print(b)
