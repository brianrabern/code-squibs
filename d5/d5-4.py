'''The function list_to_dict takes a list as its input and transforms
it into a dictionary, such that each successive pair of
values in the list becomes a key and value for the dictionary.'''

# pylint: disable-all

def list_to_dict(lst):
    d = {}

    for i in range(0,len(lst)-1,2):
        d[lst[i]] = lst[i+1]

    return d


print(list_to_dict(["a", 1, "b", 2]))
# --> {"a": 1, "b": 2}


resp = {"status": "successful",
        "data": [{"first_name": "Joe", "last_name": "Dirt"}]
        }


resp["status"] == "successful"

resp["data"] == [{"first_name": "Joe", "last_name": "Dirt"}]

resp["data"][0]["first_name"] == "Joe"

resp["data"][0]["last_name"] == "Dirt"
