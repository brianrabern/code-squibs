def comp(array1, array2):

    if array1 == None or array2 == None:
        return False

    arr1 = [abs(i) for i in array1]
    arr2 = [abs(i) for i in array2]

    x=sorted(arr1)
    y=sorted(arr2)

    x2=[i**2 for i in x]

    if y == x2:
        return True

    return False








a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a,b))
