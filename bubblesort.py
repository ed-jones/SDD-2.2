def bubbleSort(Array):
	n = len(Array)
	while (True):
		swapped = "false"
		for i in range(1, n):
			if (Array[i-1] > Array[i]):
				Array[i], Array[i-1] = Array[i-1], Array[i]
				swapped = "true"
		if (swapped == "false"):
			break
	return Array

A = [69,4,16,2,7,18,25,3]
print (bubbleSort(A))