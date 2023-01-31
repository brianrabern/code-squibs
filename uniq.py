def unique_elements(items):
    nlist =[]

    for item in items:
        if item not in nlist:
            nlist.append(item)
    return nlist

print(unique_elements([]))
print(unique_elements(["a", "a", "a"]))
print(unique_elements(["a", "a", "b"]))
