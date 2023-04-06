def fizzbuzz(maximum):
    arr = []

    for num in range(1, maximum+1):
        if (num % 3 == 0) and (num % 5 == 0):
            arr.append('fizzbuzz')
        elif (num % 3 == 0):
            arr.append('fizz')
        elif (num % 5 == 0):
            arr.append('buzz')
        else:
            arr.append(str(num))

    return arr


print(fizzbuzz(15))
