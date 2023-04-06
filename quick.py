def reverse_prefix(s, letter):
    if letter not in s:
        return s
    chunks = s.split(letter, 1)
    return letter+chunks[0][::-1]+chunks[1]


def is_double_reversible(num):
    return num % 10 != 0 if num != 0 else True







print(reverse_prefix('xyxzxe', 'z'))

print(reverse_prefix('abcdefd', 'd'))

print(reverse_prefix('abcd', 'z'))


print(is_double_reversible(526))
print(is_double_reversible(1800))
print(is_double_reversible(0))
print(is_double_reversible(770))
