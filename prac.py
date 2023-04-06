
# flake8: noqa
# pylint: disable


#python

from  functools import reduce

def mean2(numbers):
    return reduce(lambda x,y: x+y, numbers)/len(numbers)
