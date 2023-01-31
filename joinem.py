def join_numbers(digits):
    numeral = ''

    for x in digits:
        numeral += str(x)
    return numeral


print(join_numbers([]))
print(join_numbers([1]))
print(join_numbers([1, 2]))
print(join_numbers([3, 2, 1]))
