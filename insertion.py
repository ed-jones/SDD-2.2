def insertion(array):
    for i in range(1,len(array)):
        j = i
        while (j>0 and array[j-1] > array[j]):
            array[j], array[j-1] = array[j-1], array[j]
            j = j - 1
    return array

print(insertion([1,5,4,3,2,10,61,54,23]))