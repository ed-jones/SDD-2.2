"Binary Search"

import math

def binsearch(array):
    "Searches for a number using the binary search algorithm"
    print("Enter input:")
    inp = input()
    left = 0
    right = len(array - 1)
    mid = int(math.floor((left+right)/2))
    while array[mid] != inp and mid > 0:
        if  array[mid] < inp:
            mid += 1
        elif array[mid] > inp:
            mid -= 1
    if array[mid] != inp:
        mid = "not found"
    return mid

print(binsearch([1, 5, 6, 10, 15, 16, 17, 20]))
