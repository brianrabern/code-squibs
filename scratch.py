import requests
import math


def get_fact(num):
    z = math.floor(num)
    url = f"http://numbersapi.com/{z}?json"
    x=requests.get(url)
    a = x.json()
    d = a["text"]
    return d
    # a = junk["text"]
    # return a

print(get_fact(10.5))

    # d={}
    # resp = requests.get('https://randomuser.me/api')
    # data =resp.json()
    # first = data["results"][0]["name"]["first"]
    # last = data["results"][0]["name"]["first"]
    # email = data["results"][0]["email"]
    # d = {"name": f"{first} {last}", "email": email}

# def get_location_photo(city, state):

#     headers = {'Authorization': 'q0pXllnD5XxUXSPaFf03zOVUWuexXPqPv6RyER6mQsZ6BNMurld4oMBs'}

#     resp = requests.get(f"https://api.pexels.com/v1/search?query={city}+{state}", headers=headers)
#     data = resp.json()
#     location_url = data["photos"][0]["url"]
#     return location_url
