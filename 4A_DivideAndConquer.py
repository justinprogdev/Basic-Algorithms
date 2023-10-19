import math

from urllib3 import Retry

x=1680 * 640

def ueclid(length, width):
    """Finds the largest square to evenly
    divide into a larger square"""
    if length > width:
        length = length - width
    elif width > length:
        width = width - length

    #base
    mod = x % (length)
    if mod == 0 and length == width:
        return length * width
    else:
        return ueclid(length, width)

ueclid(1680, 640)
