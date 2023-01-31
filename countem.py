def count_entries(line, separator):
    x = line.split(separator)
    return len(x)


print(count_entries(",",","))
print(count_entries("a",","))
print(count_entries("a,b,c",":"))
print(count_entries("","w"))
