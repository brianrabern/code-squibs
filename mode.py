def mode(numbers):
    d = {}

    for num in numbers:
        if num not in d:
            d[num] = 1
        else:
            d[num]+=1
    most = 0
    m = 0

    for key in d:
        if d[key] > most:
            most = d[key]
            m = key

    return m








a = [1, 1, 2, 3]
b = [3, 2, 1, 3]
c = [10]
f= [6,8,3,7,3]

print(mode(a))
print(mode(f))
