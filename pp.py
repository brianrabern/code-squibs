def find_lists_with_minimum_value(lists):
    indices = []

    m = lists[0][0]

    for lis in lists:
        for n in lis:
            if n < m:
                m = n

    for lis in lists:
        if m in lis:
            indices.append(lists.index(lis))
    return indices










    # return [lis for lis in lists if m in lis]



b = [[7],[0,9,2],[8,1],[0,1]]

print(find_lists_with_minimum_value(b))




# OUTPUT
# [3]
