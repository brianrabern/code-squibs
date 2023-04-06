'''big_objects = new list
for each of the input space objects
    if the object's estimated diameter is less than 1, skip it
    create a new dictionary with these fields (and values) from the space-object:
        * `estimated_diameter`
        * `impact_probability`
    encoded_object = json encode the dictionary
    add encoded_object to the big_objects list
return the big_objects list'''


import json

def find_big_space_objects(space_objects):
    big_objects = []
    new = {}
    for d in space_objects:
        if d["estimated_diameter"] >= 1:
            new = {}
            new["estimated_diameter"] = d["estimated_diameter"]
            new["impact_probability"] = d["impact_probability"]
            encoded_object = json.dumps(new)
            big_objects.append(encoded_object)
    return big_objects

print(find_big_space_objects([{'estimated_diameter': 1.5, 'impact_probability': 0.0001, 'mass': 300}, {'estimated_diameter': 0.5, 'impact_probability': 0.0101, 'mass': 30}, {'estimated_diameter': 10.5, 'impact_probability': 0.1001, 'mass': 30000}]))
