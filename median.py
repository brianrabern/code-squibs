
def median(numbers):
    length= len(numbers)
    numbers.sort()

    if (length % 2)==1:
        i = round(length/2)-1
        return numbers[i]
    else:
        x = round(length/2)-1
        print(x)
        y = round(length/2)
        print(y)
        m = (numbers[x]+numbers[y])/2
        return int(m)






a = [1, 2, 3]
b = [3, 2, 1]
c = [5, 3, 1, 1]
d = [7,13,4,9]

print(median(d))
