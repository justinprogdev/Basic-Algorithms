# exercise 4.b page 56 Grokking Algorithms
from unittest import result


def sum_array(array):
    """Recursively sum all elements"""
    length = len(array)
    # drop last element
    n = length - 1
    num = array[n]

    if length == 1:
        return (num)
    else:
        return num + sum_array(array[0:n])


print(sum_array([10,4,6]))

