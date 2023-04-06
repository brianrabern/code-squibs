def sort(items):
    while True:
        x = 0
        for i in range(len(items)-1):

            if items[i] > items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
                x = 1

        if x == 0:
            break
    return items


print(sort([4,2,6,7,1,8]))
