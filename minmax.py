arr = [0,1,2,4,5,2,100,-3]

def max(arr):
	m = 0
	i = 0
	while i < len(arr):
		if arr[i] > m:
			m = arr[i]
		i += 1
	print "Max:", m

def min(arr):
	m = 0
	i = 0
	while i < len(arr):
		if arr[i] < m:
			m = arr[i]
		i += 1
	print "Min:", m

max(arr)
min(arr)