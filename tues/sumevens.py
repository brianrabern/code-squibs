def sum_evens(numbers):
    esum = 0
    for n in numbers:
        if not (n % 2):
            esum += n
    return esum


print(sum_evens([]))
print(sum_evens([3, 7]))
print(sum_evens([4, 7]))
print(sum_evens([1, 2, 3, 4, 5, 6]))
