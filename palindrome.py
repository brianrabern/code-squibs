
def is_palindrome(word):
    word = word.lower()
    rev_list = reversed(word)
    rev = "".join(rev_list)
    if word == rev:
        return True
    else:
        return False
    

print(is_palindrome("god"))
print(is_palindrome("racecar"))
print(is_palindrome("Hannah"))
print(is_palindrome("121"))