from random import randint


def create_list_of_four_unique_numbers():
    my_list = []

    while len(my_list) < 4:
        num = randint(1, 9)
        if num not in my_list:
            my_list.append(num)
    return my_list


print(create_list_of_four_unique_numbers())


def count_exact_matches(x, y):
    counter = 0
    pairs = zip(x, y)
    for a, b in pairs:
        if a == b:
            counter += 1
    return counter


print(count_exact_matches([2, 5, 4, 1], [3, 5, 2, 1]))


def count_common_entries(x, y):
    count = 0
    for i in x:
        for j in y:
            if i == j:
                count += 1
    return count


print(count_common_entries([1, 2, 3, 4], [5, 6, 7, 8]))


def parse_numbers(string):
    integer_list = []
    for i in string:
        integer_list.append(int(i))

    return integer_list


print(parse_numbers("1234"))
