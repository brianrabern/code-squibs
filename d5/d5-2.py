'''The function dict_to_list takes a dictionary as its input and transforms
the dictionary into a list by adding its keys and values to the list.'''



def dict_to_list(the_dict):
    mlist = []

    for key, value in the_dict.items():
        mlist.append(key)
        mlist.append(value)

    return mlist



print(dict_to_list({"a": 1, "b": 2}))
# --> ["a", 1, "b", 2]
