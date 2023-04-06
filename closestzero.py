def closest_to_zero(nums):
    # set some arbitrriy high intial values
    winpos = float('inf')
    winneg = float('inf')
    win = float('inf')

    # find the positive number closest to 0
    for i in nums:
        if (i > 0) and (abs((0 - i)) < winpos):
            winpos = i

    # find the negative number closest to 0
    for i in nums:
        if (i < 0) and abs((0 + i)) < winneg:
            winneg = i

    # give back the number whose abs value is closest to 0.
    # if there is a tie return the positive one
    if 0 in nums:
        win = 0
    elif abs(winneg) == winpos:
        win = winpos
    elif abs(winpos) < winneg:
        win = winpos
    elif abs(winneg) < winpos:
        win = winneg

    return win




print(closest_to_zero([4, 2, -1, 1, 5, 6]))
