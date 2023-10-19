from cmath import log
import math
#Binary Sort Page 8 
#binary_search takes a sorted array, and an item
#If the item is in the array, it returns its position
#We keep track of what part of the array you'll have to sort through
def binary_search(list,item):
    low = 0
    high = len(list) -1

    while low <= high:
        #each time, I check the middle element
        mid = (low + high) // 2
        guess = list[mid]

        #report - watch the mid move
        print("Guess "+ str(item) + " Mid "+ str(mid))

        #if guess is too low, update low accordingly
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

myList = [1,3,5,7,9,15,20,25,26,29,30,32,33,39,100,150,151,152]

print(binary_search(myList,151))
print(binary_search(myList,10))

print("excercise 1. What are max steps for binary search (Log2) on 128 name list")
print("Answer: "+ str(math.log2(128))) # = 7

print("exercise 2. If I double the list, what will be max steps")
print("Answer: "+ str(math.log2(256))) # = 8

#Compare 1 billion elements with binary vs linear at 1 ms per check. 
#1ms * 1 billion is 1,000,000,000 seconds
print("ms: "+ str(math.log2(1000000000))) #Binary search of 1 billion at 1 ms per, is 29.9 ms

#Linear and Binary runtimes do NOT grow at the same rate


