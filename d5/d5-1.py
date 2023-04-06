import json

def decode_and_pluck(input_json, fields):
    plucked = {}
    data= json.loads(input_json)

    for x in fields:
        # if x in input_json:
        plucked[x] = data[x]
    return plucked




print(decode_and_pluck('{"a": 1, "b": 2, "c": 3}', ["a", "c"]))
