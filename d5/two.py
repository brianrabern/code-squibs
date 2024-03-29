# This function takes a list of dictionaries (items) and a list of fields (fields).

# It should return a copy of items where each dictionary only contains the fields listed in fields.

# Example:
# items = [
#     {"a": 1, "b":2, "c": 3},
#     {"a":3, "size": 4},
#     {"b": 5, "d": 7}
# ]
# fields = ["a", "b"]
# result = just_these_fields(items, fields)
# print(result) # -->
# # [
# #     {"a": 1, "b": 2},
# #     {"a":3},
# #     {"b": 5}
# # ]

def just_these_fields(items, fields):
    result = []

    for dic in items:
        temp ={}
        for key,value in dic.items():
            if key in fields:
                temp[key] = value
        result.append(temp)
    # loop over the things, do something with each one

    return result

items = [
    {"a": 1, "b":2, "c": 3},
    {"a":3, "size": 4},
    {"b": 5, "d": 7}
]

fields = ["a", "b"]

print(just_these_fields(items, fields))
