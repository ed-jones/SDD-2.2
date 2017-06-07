"Bubble Sort Program"

def bubble_sort(array):
    "Sorts an array using the bubble sort algorithm"
    while True:
        swapped = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
                swapped = True
        if not swapped:
            break
    return array

A = [69, 4, 16, 2, 7, 18, 25, 3]
print(bubble_sort(A))
