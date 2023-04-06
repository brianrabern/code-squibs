# items = [
#     {"color":"blue", "size":"small"},
#     {"color":"red", "size":"small"},
#     {"color":"purple", "size":"medium"},
#     {"color":"green", "size":"large"},
# ]
# filters = {
#     "color": "blue",
#     "size": "medium"
# }

# result = only_items_with(items, filters)
# print(result) # --> [
#     {"color":"blue", "size":"small"},
#     {"color":"purple", "size":"medium"},
# ]


def only_items_with(items, filters):
    result = []

    for dic in items:
        temp ={}
        for key in dic:
            if (key,dic[key]) in filters.items():
                temp = dic
        if temp != {}:
            result.append(temp)
    # loop over the things, do something with each one

    return result



items = [
    {"color":"blue", "size":"small"},
    {"color":"red", "size":"small"},
    {"color":"purple", "size":"medium"},
    {"color":"green", "size":"large"},
]

filters = {
    "color": "blue",
    "size": "medium"
}

print(only_items_with(items, filters))
