
# minimal example: json to dict and back again
import json

print(type(json.loads('{"title": "Hench", "author": "Natalie Zina Walschots", "sold": 513000}')),json.loads('{"title": "Hench", "author": "Natalie Zina Walschots", "sold": 513000}'))
# a = '{"name": "John", "age": 32}'

# dict_a = json.loads(a)
# print(type(dict_a), dict_a)

# json_a = json.dumps(dict_a)
# print(type(json_a), json_a)
