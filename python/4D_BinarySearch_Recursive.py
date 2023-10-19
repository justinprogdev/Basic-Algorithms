from cmath import log
import math

# Binary Sort Page 59
# binary_search takes a sorted array, and an item
# If the item is in the array, it returns its position
# We keep track of what part of the array you'll have to sort through
def binary_search(list, item):
    #validate list
    if len(list) == 0 or item == None:
        return
        
    low = 0
    high = len(list) - 1

    #check the middle element
    try:
        mid = (low + high) // 2
        guess = list[mid]
    except:
        ""

    #base case
    if (guess == item):
        return guess
    else:
        if guess > item:
            return binary_search(list[0 : mid -1], item)
        else:
            return binary_search(list[mid + 1 : len(list)], item)


myList = [1, 3, 5, 7, 9, 15, 20, 25, 26, 29, 30, 32, 33, 39, 100, 150, 151, 152,153]

"Prints 151"
print(binary_search(myList, 151))
"prints none"
print(binary_search(myList, 10))
"prints 1"
print(binary_search(myList,1))
