def make_sentence(*words):
    sentence = ""
    for word in words:
        sentence = sentence + word + " "
    return sentence


test = make_sentence("Hello", "Programmers!", "What's up?")
print(test)


def test(z):
    print(z)
    return


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "5": 1964
}

test(thisdict)


print(thisdict)
