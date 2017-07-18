"Insertion Program"

def insertion(array):
    "Returns a sorted array"
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j = j - 1
    return array

INPUT_DECIMALS = [ord(c) - 96 for c in input()]
SORTED_DECIMALS = insertion(INPUT_DECIMALS)
SORTED_CHARS = [chr(c + 96) for c in SORTED_DECIMALS]
SORTED_STRING = ''.join(SORTED_CHARS)

print(SORTED_STRING)
