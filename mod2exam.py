
def simple_search(values, search_term):
    if search_term in values:
        return True
    return False



# def key_in_dict(list_of_dicts, key):

#     result = []

#     for d in list_of_dicts:
#         if key in d:
#             result.append(True)
#         else:
#             result.append(False)
#     return result


# print(key_in_dict([], 'color'))

# [] name
# [{'foo': 1}, {'bar': 2}] name
# [{'foo': 1}, {'color': 'orange'}] color
# [{'color': 'aubergine'}, {'color': 'orange'}, {}] color
# [{'color': 'aubergine'}, {'color': 'orange'}] color

# def uppercase_list(values):
#     result = list(map(lambda x: x.upper(), values))
#     return result


# def multiply_map(values, multiplier):
#     result = list(map(lambda x: x * multiplier, values))
#     return result

# # import json


# def key_for_value(json_string, property_value):
#     d = json.loads(json_string)

#     if key, property_value in d.items():
#         return key
#     return None


# print(key_for_value('{"name": "Noor"}', "Noor"))
