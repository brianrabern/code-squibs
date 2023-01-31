def find_longest(list):
    if list == []:
        return None

    long = ''

    for word in list:
        if len(word) > len(long):
            long = word
    return long


print(find_longest([]))
print(find_longest(["banana"]))

print(find_longest(["camping", "stove", "sock"]))
