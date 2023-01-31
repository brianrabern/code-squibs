def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_num = 0

    for char in word:
        if char in vowels:
            vowel_num = vowel_num + 1
    return vowel_num


def count_vowels_alt(word):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_num = 0

    for i in range(len(word)):
        for j in range(len(vowels)):
            if word[i] == vowels[j]:
                vowel_num = vowel_num + 1
    return vowel_num


test_word = "supercalifragilisticexpialidocious"

print(count_vowels(test_word))
print(count_vowels_alt(test_word))


def f(x):
    return x+2


def create_player_name(name):
    return name.lower().replace(" ", "-")


player = create_player_name("Wes Appleget")
print(player)

print(f(4))
