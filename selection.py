def selection(array):
    n = len(array)
    for j in range(n-1):
        iMin = j
        for i in range(j+1,n):
            if (array[i] < array[iMin]):
                iMin = i
        array[j], array[iMin] = array[iMin], array[j]
        

    return array

print(selection([22,43,111,1,23,67]))