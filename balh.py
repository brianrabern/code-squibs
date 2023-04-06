def filter_between(values, lower, upper):
    x = filter(lambda x: x >= lower and x <= upper, values)
    return list(x)



print(filter_between([1, 10, 20],70,80))

# def filter_less_than_or_equal_to(values, threshold):
#     x = filter(lambda x: x <= threshold, values)
#     return list(x)


# The function must return a new list that contains entries from
# the original list that are greater than or equal to the lower
# threshold value and less than or equal to the upper threshold value.
