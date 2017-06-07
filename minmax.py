"Min/Max Program"

def print_max(arr):
    "Prints maximum value in an array"
    maximum = 0
    for i in enumerate(arr):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

def print_min(arr):
    "Prints the minimum value in an array"
    minimum = 0
    for i in enumerate(arr):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum

ARRAY = [0, 1, 2, 4, 5, 2, 100, -3]
print("Max:", max(ARRAY))
print("Min:", min(ARRAY))
