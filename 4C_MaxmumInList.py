def max_list(array,top):
    """Find maximum in list"""
    length = len(array)
    n = length - 1
    if length == 0:
        return top
    else:
        if top > array[n]:
            return max_list(array[0:n],top)
        else:
            return max_list(array[0:n],array[n])



high = max_list([15,10,5], 0)
print(high)
input()