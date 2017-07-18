"Selection Sort"

def selection(array):
    "sorts an array based on size"
    for j in range(len(array)-1):
        imin = j
        for i in range(j+1, len(array)):
            if array[i] < array[imin]:
                imin = i
        array[j], array[imin] = array[imin], array[j]

    return array

LIST = ["aa", "a", "aaa", "aaaa", "aaaaa"]



print(selection(LIST))
