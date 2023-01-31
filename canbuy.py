def can_buy_ticket(person):
    if person["age"] >= 21:
        return True
    if (person["state"] == "NV" or person["state"] == "NJ") and person["age"] >= 18:
        return True
    else:
        return False


print(can_buy_ticket({ "age" : 18, "state": "NV" }))

print(can_buy_ticket({ "age" : 25 }))


# The function will return True if someone lives in NV or NJ, and is 18 years or older. It will also return True if someone is 21 years or older from any state. Otherwise, it will return False.

# Please fix the function below so that it will pass its unit tests and not fail when the "state" key is missing or non-existent.

# def can_buy_ticket(person):
#     if person["state"] == "NV" and person["state"] == "NJ" or person["age"] >= 21:
#         return True
#     else:
#         return False
