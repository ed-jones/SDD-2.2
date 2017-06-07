"Min/Max Program"

def array_max(arr):
    "Return maximum value in an array"
    maximum = 0
    for i in enumerate(arr):
        if arr[i[0]] > maximum:
            maximum = arr[i[0]]
    return maximum

def array_min(arr):
    "Return the minimum value in an array"
    minimum = 0
    for i in enumerate(arr):
        if arr[i[0]] < minimum:
            minimum = arr[i[0]]
    return minimum

ARRAY = [0, 1, 2, 4, 5, 2, 100, -3]
print("Max:", array_max(ARRAY))
print("Min:", array_min(ARRAY))
