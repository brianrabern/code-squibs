def sort(sentence):
    new_sentence = ""

    if len(sentence) == 0:
        return new_sentence

    nums= "123456789"
    dictionary = {}

    for word in sentence.split():
        for x in word:
            if x in nums:
                dictionary[int(x)] = word

    for i in range(1,10):
        new_sentence += dictionary.get(i, "") + " "

    return new_sentence



print(sort("Thi4s i3s fu2n hh1j"))
