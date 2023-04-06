import math


def find_larger_area(s, r):
    square = s * s
    circle = math.pi * r * r
    if square > circle:
        return "SQUARE"
    elif square < circle:
        return "CIRCLE"


print(find_larger_area(6, 2))
print(find_larger_area(12, 124))


def does_product_exist(nums, left, right, target):
    for i in range(left, right+1):
        for j in range(i + 1, right+1):
            if nums[i] * nums[j] == target:
                return True
    return False


print(does_product_exist([1, 5, 5, 2, 3], 0, 2, 25))
print(does_product_exist([1, 5, 5, 2, 3], 0, 1, 25))


def make_integer(nums, length):
    sort_nums = sorted(nums)
    x = ''.join(str(c) for c in sort_nums)
    cut = x[:length]
    return int(cut)


print(make_integer([3, 1, 2, 6, 5, 9], 5))
