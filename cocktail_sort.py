

def cocktail_sort(items):
    '''bidirectional bubble sort'''
    while True:
        made_a_swap = False

        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                made_a_swap = True

        if not made_a_swap:
            break

        for i in range(len(items)-1, 0, -1):
            if items[i] < items[i-1]:
                items[i], items[i-1] = items[i-1], items[i]
                made_a_swap = True

        if not made_a_swap:
            break

    return items


print(cocktail_sort([4, 2, 6, 7, 1, 8]))

#https://upload.wikimedia.org/wikipedia/commons/e/ef/Sorting_shaker_sort_anim.gif
